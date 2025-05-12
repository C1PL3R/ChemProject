from django.shortcuts import render, redirect
from django.views import View
from core.models import Contact


class ChatView(View):
    def get(self, request):
        if request.user.is_authenticated:
            contact_list = Contact.objects.filter(user=request.user.id)
            if not contact_list:
                contact_list = Contact.objects.filter(contact=request.user.id)

            if contact_list:
                contact = contact_list.first()

                if contact.user == request.user:
                    receiver = contact.contact
                    sender = contact.user
                else:
                    receiver = contact.user
                    sender = contact.contact

                context = {
                    'contacts': contact_list,
                    'receiver_name': receiver.username,
                    'title': 'ChemChat',
                }

                return render(request, 'ChemChat/chat.html', context)
            else:
                return render(request, 'ChemChat/chat.html', {'no_contacts': True, 'title': 'ChemChat'})
        else:
            return redirect('auth')




