from django.urls import path, include
from .views_classes.document_with_id_view import DocumentWithIdView
from .views_classes.document_view import DocumentView


urlpatterns = [
    path('document/', DocumentView.as_view(), name='document'),
    path('document/<str:document_id>/', DocumentWithIdView.as_view(), name='document_view')
]