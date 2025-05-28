from django.views import View
from core.models import Document
from django.http import JsonResponse
import json


class DeleteDocumentView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        try:
            data = json.loads(request.body)
            doc_id = data.get("doc_id")
            
            if not doc_id:
                return JsonResponse({'error': 'Missing document ID'}, status=400)

            Document.objects.get(id=doc_id, owner=request.user).delete()

            return JsonResponse({'success': "Document deleted successfully!"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        