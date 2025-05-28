from django.shortcuts import render, redirect
from django.views import View
from core.models import Document
from django.http import Http404


class DocumentWithIdView(View):
    def get(self, request, document_id):
        if not request.user.is_authenticated:
            return redirect('auth')

        document = Document.objects.filter(id=document_id).first()

        if document.is_private:
            if document.owner == request.user or request.user in document.allowed_users.all():
                context = {
                    'document_id': document_id,
                    'title': 'ChemDocument',
                    'document': document,
                    'document_text': document.text,
                    'icons_list_1': ['doc-icon', 'doc-profile-icon', 'document-2-icon', 'document-3-icon'],
                    'icons_list_2': ['docx-icon', 'file-icon', 'pdf-icon', 'to-do-icon'],
                }
                return render(request, 'ChemDocument/document.html', context)
            else:
                return render(request, 'ChemDocument/document.html', {'document_is_private': True, 'title': 'ChemDocument'})
        else:
            context = {
                'document_id': document_id,
                'title': 'ChemDocument',
                'document': document,
                'document_text': document.text,
                'icons_list_1': ['doc-icon', 'doc-profile-icon', 'document-2-icon', 'document-3-icon'],
                'icons_list_2': ['docx-icon', 'file-icon', 'pdf-icon', 'to-do-icon'],
            }
            return render(request, 'ChemDocument/document.html', context)