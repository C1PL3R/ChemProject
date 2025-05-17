from core.models import Chemist
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse  
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
import json
import re


def remove_formatting(phone_number):
    cleaned = re.sub(r'\D', '', phone_number)
    return cleaned

class AuthView(View):
    def get(self, request):
        return render(request, 'auth.html')
    
class AuthPostView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone')
        phone = remove_formatting(phone_number)
                
        if not username or not password:
            return JsonResponse({'message': 'Username або пароль не можуть бути порожніми!'}, status=400)

        try:
            user = Chemist.objects.get(username=username)
            if check_password(password, user.password):
                login(request, user)
                print("Паролі збігаються!")
                return JsonResponse({'redirect_url': reverse('chat')})
            else:
                return JsonResponse({'message': 'Пароль не збігається!'}, status=400)
        except Chemist.DoesNotExist:
            if Chemist.objects.filter(username=username, phone=phone).exists():
                user = Chemist.objects.get(username=username, phone=phone)
                login(request, user)
                redirect('chat')

            user, created = Chemist.objects.get_or_create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone
            )

            if created:
                user.set_password(password)
                user.save()

            login(request, user)
            return JsonResponse({'redirect_url': reverse('chat')})