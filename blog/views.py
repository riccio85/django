from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
#published_date__lte sta per published_date + lessthanorequals e -published_date per ordine decrescentea
#gli oggetti in pthon si chiamano dictionary simile a oggetti javascript, ma dove la chiave puo essere qualsiasi cosa hashble
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})