from django.contrib.auth.models import User
from django.db import models
from  django.shortcuts import reverse

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))


    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250 , unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES , default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.created_date.year, self.created_date.strftime('%m'), self.created_date.strftime('%d'), self.slug])



