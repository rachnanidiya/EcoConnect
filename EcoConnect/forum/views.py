from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ForumPost, ForumComment

def forum_list(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum_list.html', {'posts': posts})


@login_required
def forum_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    comments = post.comments.all().order_by('created_at')

    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            ForumComment.objects.create(
                post=post,
                author=request.user,
                text=text
            )
            return redirect('forum:forum_detail', post_id=post.id)

    return render(request, 'forum_detail.html', {
        'post': post,
        'comments': comments
    })

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            ForumPost.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            return redirect('forum:forum_list')
    return render(request, 'create_post.html')