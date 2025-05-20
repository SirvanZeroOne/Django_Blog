from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'author' , 'created_date' , 'status',)
    list_filter = ('title',  'author' ,  'status',)
    search_fields = ('title', ' author',)


# Register your models here.
admin.site.register(models.Post , PostAdmin)