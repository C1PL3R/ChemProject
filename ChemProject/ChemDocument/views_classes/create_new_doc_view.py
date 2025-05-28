from django.views import View
from core.models import Document
from django.http import JsonResponse
import json


class CreateNewDocView(View):
    def post(self, request):
        data = json.loads(request.body)
        title = data.get("title")
        icon = data.get("icon")

        if not title:
            title = "Документ Без Назви"
        if not icon:
            icon = "doc-icon"

        curent_user = request.user

        doc = Document.objects.create(title=title, owner=curent_user, icon=icon)

        context = {
            "doc": {
                "id": doc.id,
                "title": doc.title,
                "icon": doc.icon,
            }
        }

        return JsonResponse(context, status=200)