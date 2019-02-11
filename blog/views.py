from django.shortcuts import render
from .models import Post


# posts = [
#     {
#         'author': 'Dave',
#         'title': 'Post 1',
#         'content': 'My first blog post.',
#         'date_posted': 'January 8, 2019'
#     },
#     {
#         'author': 'Sammie',
#         'title': 'Post 2',
#         'content': 'Second blog post.',
#         'date_posted': 'January 19, 2019'
#     },
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

