from django.db import models
from core.models import Chemist

class Contact(models.Model):
    user = models.ForeignKey(Chemist, on_delete=models.CASCADE, related_name='user_contacts')
    contact = models.ForeignKey(Chemist, on_delete=models.CASCADE, related_name='contact_users')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'contact')      
    
    def __str__(self):
        return f"{self.user.username} - {self.contact.username}"
    