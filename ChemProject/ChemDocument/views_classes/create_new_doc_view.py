from django.views import View
from core.models import Document
from django.http import JsonResponse


class CreateNewDocView(View):
    def post(self, request):
        curent_user = request.user
        
        doc = Document.objects.create(title="Документ Без Назви", creator=curent_user)
        
        context = {
            "doc": {
                "id": doc.id,
                "title": doc.title,
            }
        }
        
        return JsonResponse(context, status=200)
