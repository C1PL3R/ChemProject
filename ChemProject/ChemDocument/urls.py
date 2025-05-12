from django.urls import path
from .views_classes.document_with_id_view import DocumentWithIdView
from .views_classes.document_view import DocumentView
from .views_classes.create_new_doc_view import CreateNewDocView


urlpatterns = [
    path('', DocumentView.as_view(), name='document'),
    path('create-new-doc/', CreateNewDocView.as_view()),
    path('<str:document_id>/', DocumentWithIdView.as_view(), name='document_with_id'),
]