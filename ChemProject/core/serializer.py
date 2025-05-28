from rest_framework import serializers
from core.models import Molecule

class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = ["id", "name", "formula", "created_at"]
        read_only_fields = ["id"]


        