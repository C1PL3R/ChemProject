from django.shortcuts import render, redirect
from django.views import View
from core.models import Document, Chemist
from django.http import JsonResponse
import json

class AddAllowedUserView(View):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)
                id = data.get('doc_id')
                
                document = Document.objects.get(id=id)
                
                if document.owner != request.user:
                    return JsonResponse({'error': 'You are not the owner of this document.'}, status=403)
                else:
                    email = data.get('user_email')
                    
                    chemist = Chemist.objects.filter(email=email).first()
                    
                    if not chemist:
                        return JsonResponse({'error': 'User not found.'}, status=404)
                    else:
                        document.is_private = True
                        document.allowed_users.add(chemist)
                        document.save()

                        return JsonResponse({'success': "This user has been successfully granted access to view the document!"})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return redirect('auth')

