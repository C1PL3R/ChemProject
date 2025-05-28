from django.shortcuts import render, redirect
from django.views import View
from core.models import Contact
from django.db.models import Q


def get_contacts_data(request):
    contact_list = Contact.objects.filter(user=request.user.id)
    if not contact_list.exists():
        contact_list = Contact.objects.filter(contact=request.user.id)

    contacts_data = []

    for contact in contact_list:
        if contact.user == request.user:
            contact_object = contact.contact
        else:
            contact_object = contact.user

        chat = Contact.objects.filter(
            Q(user=request.user, contact=contact_object) |
            Q(user=contact_object, contact=request.user)
        ).first()

        contacts_data.append({
            "username": contact_object.username,
            "phone": contact_object.phone,
            "id": contact_object.id,
            "chat_id": chat.id
        })
    print(contacts_data)

    return contacts_data

class ChatView(View):
    def get(self, request):
        if request.user.is_authenticated:
            contacts_data = get_contacts_data(request)
            
            if contacts_data:
                context = {
                    'contacts': contacts_data,
                    'title': 'ChemChat',
                }
                return render(request, 'ChemChat/chat.html', context)
            else:
                return render(request, 'ChemChat/chat.html', {'no_contacts': True, 'title': 'ChemChat'})
        else:
            return redirect('auth')




