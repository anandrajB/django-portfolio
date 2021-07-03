from django.contrib import admin
from .models import contact , files
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(contact)
admin.site.register(files)
admin.site.unregister(Group)