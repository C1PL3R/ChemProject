from django.shortcuts import render, redirect
from django.views import View
from core.models import Document


class DocumentWithIdView(View):
    def get(self, request, document_id):
        if request.user.is_authenticated:
            doc = Document.objects.filter(id=document_id).first()
            
            context =  {'document_id': document_id, 
                        'title': 'ChemDocument',
                        'document': doc}
            
            return render(request, 'ChemDocument/document.html', context)
        else:
            return redirect('auth')

