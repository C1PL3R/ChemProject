from django.urls import path
from .views_classes.document_with_id_view import DocumentWithIdView
from .views_classes.document_view import DocumentView
from .views_classes.create_new_doc_view import CreateNewDocView
from .views_classes.delete_document_view import DeleteDocumentView
from .views_classes.save_settings_view import SaveSettingsView
from .views_classes.add_allowed_user_view import AddAllowedUserView


urlpatterns = [
    path('', DocumentView.as_view(), name='document'),
    path('create-new-doc/', CreateNewDocView.as_view()),   
    path('delete-document/', DeleteDocumentView.as_view()),
    path('save-settings/', SaveSettingsView.as_view()),
    path('add-allowed-user/', AddAllowedUserView.as_view()),

    path('<str:document_id>/', DocumentWithIdView.as_view(), name='document_with_id'),
]