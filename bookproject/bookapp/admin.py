from django.contrib import admin
from .models import RegisterBook

# Register your models here.

class Bookadmin(admin.ModelAdmin):
    list_display =["coverphoto","title", "author","description"]
    
admin.site.register(RegisterBook,Bookadmin)