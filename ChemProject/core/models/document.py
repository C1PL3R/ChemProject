from django.db import models
from .chemist import Chemist


class Document(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    creator = models.ForeignKey('Chemist', on_delete=models.CASCADE, related_name='creator')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
