from django.shortcuts import render


def view_molecule(request):
    return render(request, 'ChemVisualizer/view_molecule.html')


def visualize_file(request):
    return render(request, 'ChemVisualizer/visualize_file.html')
