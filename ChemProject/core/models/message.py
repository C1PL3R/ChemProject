from django.db import models

class Message(models.Model):
    sender = models.ForeignKey('Chemist', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey('Chemist', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    chat_id = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        short_content = self.content[:15].rsplit(" ", 1)[0]
        return f"Sender: {self.sender.username} Receiver: {self.receiver.username} Content: {short_content}"