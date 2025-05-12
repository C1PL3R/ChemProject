from django.shortcuts import render, redirect
from django.views import View
from core.models import Contact


class DocumentWithIdView(View):
    def get(self, request, document_id):
        if request.user.is_authenticated:
            return render(request, 'document.html', {'document_id': document_id})
        else:
            return redirect('auth')

