from django.views import View
from core.models import Document
from django.http import JsonResponse


class CreateNewDocView(View):
    def post(self, request):
        curent_user = request.user
        
        doc = Document.objects.create(title="Безіменний документ", creator=curent_user)
        
        return JsonResponse({'doc_id': doc.id}, status=200)
