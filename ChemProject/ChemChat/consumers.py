from channels.generic.websocket import AsyncWebsocketConsumer
import json
from core.models import Message, Chemist, Contact
from asgiref.sync import sync_to_async


@sync_to_async
def create_message(sender_id, receiver_id, message, contact_id):
    contact = Contact.objects.get(id=str(contact_id))

    sender_contact = Chemist.objects.filter(id=sender_id).first()
    receiver_contact = Chemist.objects.filter(id=receiver_id).first()

    sender_chemist = sender_contact
    receiver_chemist = receiver_contact

    Message.objects.create(
        sender=sender_chemist, receiver=receiver_chemist, content=message, chat_id=contact.id)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = f'chat_{self.room_name}'

        # Приєднуємо користувача до групи
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Від'єднуємо користувача від групи
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']

        print(
            f"Отримано повідомлення: {message}, Відправник: {self.sender_id}, Отримувач: {self.receiver_id}")

        await create_message(sender_id=self.sender_id, receiver_id=self.receiver_id, message=message, contact_id=self.room_name)

        # Розсилаємо повідомлення всім в кімнаті
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': self.sender_id,
                'receiver_id': self.receiver_id,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']
        receiver_id = event['receiver_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id,
            'receiver_id': receiver_id,
        }))


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

        print(f"Отримано текст: {text}")

        # Відправляємо оновлення всім користувачам групи
        await self.channel_layer.group_send(
            self.document_group_name,
            {
                'type': 'document_update',  # це type, який ви хочете обробити
                'message': text
            }
        )

    # Обробник для події 'document_update'
    async def document_update(self, event):
        text = event['message']

        # Надсилаємо оновлений текст клієнту
        await self.send(text_data=json.dumps({
            'text': text
        }))
