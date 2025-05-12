from django.shortcuts import render

from django.views import View
from core.models import Contact, Message


class ChatWithIDView(View):
    def get(self, request, chat_id):
        contact_list = Contact.objects.filter(user=request.user.id)
        if not contact_list:
            contact_list = Contact.objects.filter(contact=request.user.id)

        chat = contact_list.get(id=chat_id)

        if chat.user == request.user:
            receiver = chat.contact
            sender = chat.user
        else:
            receiver = chat.user
            sender = chat.contact
        
        try:
            messages_list = Message.objects.filter(chat_id=int(chat_id))
        except Exception:
            context = {
                'contacts': contact_list,
                'chat_id': chat_id,
                'sender_id': sender.id,
                'receiver_id': receiver.id,
                'sender_name': sender.username,
                'receiver_name': receiver.username,
                'receiver_phone': receiver.phone,
            }

            return render(request, 'ChemChat/chat.html', context)

        context = {
            'contacts': contact_list,
            'chat_id': chat_id,
            'sender_id': sender.id,
            'receiver_id': receiver.id,
            'sender_name': sender.username,
            'receiver_name': receiver.username,
            'receiver_phone': receiver.phone,
            'message_list': messages_list,
        }

        return render(request, 'ChemChat/chat.html', context)
