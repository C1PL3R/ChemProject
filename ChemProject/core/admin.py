from django.contrib import admin
from core.models import Chemist, Message, Contact, Molecule, Document

# Register your models here.
admin.site.register(Chemist)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Molecule)
admin.site.register(Document)