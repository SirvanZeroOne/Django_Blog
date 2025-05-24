from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'author' , 'created_date' , 'status',)
    list_filter = ('title',  'author' ,  'status',)
    search_fields = ('title', ' author',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',  'email' , 'created_date' , 'active',)
    list_filter = ('email',  'active' ,  'name',)
    search_fields = ('comment',)


# Register your models here.
admin.site.register(models.Post , PostAdmin)
admin.site.register(models.Comment , CommentAdmin)