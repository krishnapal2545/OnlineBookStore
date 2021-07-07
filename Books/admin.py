from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('adminid','bookid','name','author','genre','language','photo')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('adminid','name','logid','password')

admin.site.register(Book,BookAdmin)
admin.site.register(Admin,AdminAdmin)