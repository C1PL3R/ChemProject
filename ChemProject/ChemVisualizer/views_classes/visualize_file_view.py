from django.shortcuts import render, redirect
from django.views import View


class VisualizeFileView(View):
    def get(self, request):
        sdf_data = request.session.pop('sdf_data', None)
        return render(request, 'ChemVisualizer/visualize.html', {'sdf_data': sdf_data, 'title': 'ChemVisualizer'})
    
    def post(self, request):
        sdf_file = request.FILES['sdf_file']
        sdf_data = sdf_file.read().decode('utf-8')
        request.session['sdf_data'] = sdf_data
        return redirect('visualize_file')