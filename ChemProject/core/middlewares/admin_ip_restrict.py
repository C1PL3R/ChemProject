from django.http import HttpResponseForbidden
import os
from dotenv import load_dotenv


class AdminIPRestrictionMiddleware:
    def __init__(self, get_response):
        dotenv_path = r"D:\Vitaliy\Документи\Коди\GitHub\ChemProject\ChemProject\.env"
        load_dotenv(dotenv_path)

        raw_ips = os.getenv('MY_IP', '')
        
        self.ALLOWED_IPS = [ip.strip() for ip in raw_ips.split(',') if ip.strip()]
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            print(f"[middleware] ALLOWED_IPS: {self.ALLOWED_IPS}")
            real_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
            print(f"[admin] Request IP: {real_ip}")
            if real_ip not in self.ALLOWED_IPS:
                return HttpResponseForbidden("Access denied.")
        return self.get_response(request)
