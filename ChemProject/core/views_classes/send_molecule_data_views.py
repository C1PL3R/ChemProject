from django.views import View
from django.http import JsonResponse
import pubchempy as pcp
from pubchempy import BadRequestError
import json


class SendNameView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        results = pcp.get_compounds(name, 'name')

        if results:
            compound = results[0]
            smiles = compound.isomeric_smiles
            return JsonResponse({'status': 'success', 'name': name, 'smiles': smiles}, status=200)
        else:
            return JsonResponse({'status': 'fail', 'error': 'Сполуку не знайдено'})
    
        
class SendFormulaView(View):
    def post(self, request):
        data = json.loads(request.body)
        formula = data.get('formula')
        
        results = pcp.get_compounds(formula, namespace='formula')
        try:
            if results:
                compound = results[0]
                smiles = compound.isomeric_smiles
                name = compound.synonyms[0]
                return JsonResponse({'status': 'success', 'name': name, 'smiles': smiles}, status=200)
            else:
                return JsonResponse({'status': 'fail', 'error': 'Сполуку не знайдено'})    
        except BadRequestError:
            return JsonResponse({'status': 'fail', 'error': 'Некоректна формула'})