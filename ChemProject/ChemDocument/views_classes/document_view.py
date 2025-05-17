from django.shortcuts import render, redirect
from django.views import View
from core.models import Document


class DocumentView(View):
    def get(self, request):
        if request.user.is_authenticated:
            docs = Document.objects.filter(creator=request.user)
            return render(request, 'ChemDocument/document.html', {'docs': docs, 
                                                                  'title': 'ChemDocument', 
                                                                  'is_doc_page': True})
        else:
            return redirect('auth')

