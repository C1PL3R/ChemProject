from django.db import models

class Message(models.Model):
    sender = models.ForeignKey('Chemist', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey('Chemist', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"