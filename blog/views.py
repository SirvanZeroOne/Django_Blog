from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from taggit.models import Tag
from blog.models import Post


# Create your views here.
def post_list(request, tag_slug=None):
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(status='published' , tags__in=[tag])
    else:
        posts = Post.objects.filter(status='published')
    context = {
        'posts': posts,}
    return render(request, 'post_list.html', context)


def post_detail(request, year, month, day , slug):
    try:
        post = Post.objects.get(created_date__year=year, created_date__month=month, created_date__day=day,slug=slug,status='published')
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    comment_form = forms.comment_forms()
    new_comment = None

    if request.method == 'POST':
        comment_form = forms.comment_forms(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', year, month, day, slug)
    context = {
             'post': post,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }

    return render(request, 'post_detail.html', context)

def post_contact(request):
    return HttpResponse('<h1> CONTACT US </h1>')