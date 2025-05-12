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
        
        chemist_contact = Chemist.objects.filter(username=username, phone=phone).first()

        if not chemist_contact:
            return JsonResponse({'error': 'Користувача не знайдено!'}, status=400)

        if chemist_contact == current_user:
            return JsonResponse({'error': 'Не можна додати себе!'}, status=400)

        existing_chat = Contact.objects.filter(user=current_user, contact=chemist_contact).first()

        if existing_chat:
            return JsonResponse({'error': 'Чат із цим користувачем вже створено!'}, status=400)

        Contact.objects.create(user=current_user, contact=chemist_contact)

        return JsonResponse({'success': f'Чат створено з {chemist_contact.username}!'}, status=200)
