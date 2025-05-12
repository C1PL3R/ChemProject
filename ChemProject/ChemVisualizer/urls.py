from django.urls import path, include
from .views import visualize_file
from .views_classes.converter_view import ConvertView
from .views_classes.molecule_view import MoleculeView
from .views_classes.visualize_file_view import VisualizeFileView

urlpatterns = [
    path('view_molecule/', MoleculeView.as_view(), name='view_molecule'),
    path('converter/', ConvertView.as_view(), name='converter'),
    path('visualize_file/', VisualizeFileView.as_view(), name='visualize_file'),
]