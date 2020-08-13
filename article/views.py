from django.shortcuts import render
from .documents import PostDocument


def search(request):
    q = request.GET('q')
    if q:
        posts = PostDocument.search().query('match', title=q)
    else:
        posts = ''
    context = {
        'posts': 'posts'
    }
    template_name = 'search.html'
    return render(request, template_name, context)
