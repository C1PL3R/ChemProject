from django.shortcuts import render, redirect
from django.views import View
from core.models import Contact


class DocumentView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'ChemDocument/document.html', {'title': 'ChemDocument'})
        else:
            return redirect('auth')

