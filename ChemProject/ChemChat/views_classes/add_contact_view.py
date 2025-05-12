from django.http import JsonResponse
from django.views import View

from core.models import Chemist, Contact

import json
import re


def remove_formatting(phone_number):
    cleaned = re.sub(r'\D', '', phone_number)
    return cleaned


class AddContactView(View):
    def post(self, request):
        current_user = request.user

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Некоректні дані'}, status=400)

        username = data.get('username')
        phone_number = data.get('phone_number')
        
        phone = remove_formatting(phone_number)
        print(f"Username: {username}, Phone: {phone}")
        
        contact = Chemist.objects.filter(username=username, phone=phone).first()

        if not contact:
            return JsonResponse({'error': 'Користувача не знайдено!'}, status=400)

        contact = Contact.objects.filter(user=current_user, contact=contact).first()

        if contact:
            return JsonResponse({'error': 'Чат із цим користувачем вже створено!'}, status=400)
        else:
            Contact.objects.create(user=current_user, contact=contact)

        return JsonResponse({'success': f'Чат створено з {contact.username}!'}, status=200)
