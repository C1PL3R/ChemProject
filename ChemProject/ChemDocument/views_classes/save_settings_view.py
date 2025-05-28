from django.shortcuts import redirect
from django.views import View
from core.models import Document
from django.http import JsonResponse
import json


class SaveSettingsView(View):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)
                id = data.get("doc_id")
                document = Document.objects.filter(id=id).first()
                
                if document.owner != request.user:
                    return JsonResponse({'error': 'You are not the owner of this document.'}, status=403)
                else:
                    is_private = data.get("is_private")
                    icon = data.get("icon")
                    
                    if icon:
                        document.is_private = is_private
                        document.icon = icon
                        document.save()          

                        return JsonResponse({'success': "Document data is updated successfully!"})
                    else:
                        return JsonResponse({'error': "Missing icon!"}, status=400)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return redirect('auth')

