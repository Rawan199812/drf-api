from django.contrib import admin
from django.db import models
from .models import SpongeBob

# Register your models here.
@admin.register(SpongeBob)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
#admin.site.register(SpongeBob) # I replace it with the decorater

