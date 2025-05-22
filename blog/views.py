from django.http import HttpResponse, Http404
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(status='published')
    context = {
        'posts': posts,}
    return render(request, 'post_list.html', context)

def post_detail(request, year, month, day , slug):
    try:
        post = Post.objects.get(created_date__year=year, created_date__month=month, created_date__day=day,slug=slug,status='published')
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    context = {
             'post': post,
    }
    return HttpResponse('<h1> {} </h1>'.format(post.title))