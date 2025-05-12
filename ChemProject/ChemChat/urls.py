from django.urls import path, include
from .views_classes.chat_view import ChatView
from .views_classes.chat_with_chat_id_view import ChatWithIDView
from .views_classes.add_contact_view import AddContactView

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('chat/<str:chat_id>/', ChatWithIDView.as_view(), name='chat_with_id'),
    path('add_contact/', AddContactView.as_view(), name='add_contact'),
]