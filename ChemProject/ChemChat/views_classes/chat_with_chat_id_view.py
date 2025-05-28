from django.shortcuts import render

from django.views import View
from core.models import Contact, Message
from .chat_view import get_contacts_data


class ChatWithIDView(View):
    def get(self, request, chat_id):
        contacts_data = get_contacts_data(request)

        for contact in contacts_data:
            if contact['chat_id'] == chat_id:
                phone = contact['phone']
                username = contact['username']
                contact_id = contact['id']
                break

        try:
            messages_list = Message.objects.filter(chat_id=str(chat_id))
        except Exception:
            context = {
                'contacts': contacts_data,
                'chat_id': chat_id,
                'sender_id': request.user.id,
                'title': 'ChemChat',
                'phone': phone,
                'username': username,
                'receiver_id': contact_id,
            }

            return render(request, 'ChemChat/chat.html', context)

        context = {
            'contacts': contacts_data,
            'chat_id': chat_id,
            'sender_id': request.user.id,
            'phone': phone,
            'username': username,
            'receiver_id': contact_id,
            'message_list': messages_list,
            'title': 'ChemChat',
        }

        return render(request, 'ChemChat/chat.html', context)
