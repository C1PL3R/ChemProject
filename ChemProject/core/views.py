from django.shortcuts import render
from core.models import Molecule
import re
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializer import MoleculeSerializer
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect


def index(request):
    molucules = Molecule.objects.all()
    return render(request, 'index.html', {'molecules_history': molucules, 'title': 'ChemProject'})


def auth(request):
    if request.user.is_authenticated:
        return render(request, 'auth.html', {'title': 'ChemProject'})
    else:
        return render(request, 'auth.html', {'no_auth': True, 'title': 'ChemProject'})
    
    
def about(request):
    return render(request, 'about.html', {'title': 'ChemProject'})


def what_are_smiles(request):
    return render(request, 'what_are_smiles.html', {'title': 'ChemProject'})



def logout(request):
    django_logout(request)
    return redirect('auth')


def copyright_for_google(request):
    return render(request, 'google45b8458dd0908687.html')
    

class MoluculeAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Molecule.objects.all()
    serializer_class = MoleculeSerializer