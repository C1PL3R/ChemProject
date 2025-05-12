from django.shortcuts import render
from core.models import Molecule
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializer import MoleculeSerializer
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect


def index(request):
    molucules = Molecule.objects.all()
    return render(request, 'index.html', {'molecules_history': molucules})


def auth(request):
    if request.user.is_authenticated:
        return render(request, 'auth.html')
    else:
        return render(request, 'auth.html', {'no_auth': True})
    
    
def about(request):
    return render(request, 'about.html')


def what_are_smiles(request):
    return render(request, 'ChemVisualizer/what_are_smiles.html')



def logout(request):
    django_logout(request)
    return redirect('index')
    

class MoluculeAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Molecule.objects.all()
    serializer_class = MoleculeSerializer