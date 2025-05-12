from django.urls import re_path
from ChemChat.consumers import ChatConsumer, DocumentConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_id>\w+)/$', ChatConsumer.as_asgi()),
    re_path(r'ws/document/(?P<document_id>\w+)/$', DocumentConsumer.as_asgi())
]