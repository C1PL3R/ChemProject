from django.shortcuts import render, redirect
from django.views import View
from core.models import Document


class DocumentView(View):
    def get(self, request):
        if request.user.is_authenticated:
            docs = Document.objects.filter(owner=request.user)
            
            context = {
                'docs': docs,
                'title': 'ChemDocument',
                'is_doc_page': True,
                'icons_list_1': ['doc-icon', 'doc-profile-icon', 'document-2-icon', 'document-3-icon'],
                'icons_list_2': ['docx-icon', 'file-icon', 'pdf-icon', 'to-do-icon'],
            }
            
            return render(request, 'ChemDocument/document.html', context)
        else:
            return redirect('auth')

