from django.db import models
from .chemist import Chemist


class Document(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    owner = models.ForeignKey('Chemist', on_delete=models.CASCADE, related_name='owner', null=True)
    icon = models.CharField(max_length=20, default='doc-icon')
    date = models.DateTimeField(auto_now_add=True)
    allowed_users = models.ManyToManyField(Chemist, blank=True, related_name='accessible_documents')
    is_private = models.BooleanField(default=True)
    is_show = models.BooleanField(default=True)

    def __str__(self):
        return self.title
