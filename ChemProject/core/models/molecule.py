from django.db import models

class Molecule(models.Model):
    name = models.CharField(max_length=100)
    formula = models.CharField(max_length=50)
    smiles = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name