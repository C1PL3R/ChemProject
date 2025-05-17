from channels.generic.websocket import AsyncWebsocketConsumer
import json
from core.models import Document
from asgiref.sync import sync_to_async


@sync_to_async
def save_doc(text, doc_id):
    Document.objects.filter(id=doc_id).update(text=text)


@sync_to_async
def save_doc_title(title, doc_id):
    Document.objects.filter(id=doc_id).update(title=title)

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.document_name = self.scope['url_route']['kwargs']['document_id']
        self.document_group_name = f'document_{self.document_name}'

        # Приєднуємо користувача до групи
        await self.channel_layer.group_add(
            self.document_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Від'єднуємо користувача від групи
        await self.channel_layer.group_discard(
            self.document_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        text = data.get('text')
        title = data.get('title')

        if text:
            print("Текст збережено!")
            await save_doc(text=text, doc_id=int(self.document_name))
            await self.channel_layer.group_send(
                self.document_group_name,
                {
                    'type': 'document_update',
                    'message': text
                }
            )
        elif title:
            print(f"Отримано заголовок: {title}")
            await save_doc_title(title=title, doc_id=int(self.document_name))
            
            await self.channel_layer.group_send(
                self.document_group_name,
                {
                    'type': 'document_title',
                    'message': title
                }
            )


    async def document_update(self, event):
        text = event['message']

        await self.send(text_data=json.dumps({
            'text': text
        }))

    async def document_title(self, event):
        text = event['message']

        await self.send(text_data=json.dumps({
            'text': text
        }))
