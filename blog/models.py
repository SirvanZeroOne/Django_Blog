from django.contrib.auth.models import User
from django.db import models
from  django.shortcuts import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))


    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250 , unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES , default='draft')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def active_comments(self):
        return  self.comment_set.filter(active=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.created_date.year, self.created_date.strftime('%m'), self.created_date.strftime('%d'), self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return '{} by {}'.format(self.name, self.name)



