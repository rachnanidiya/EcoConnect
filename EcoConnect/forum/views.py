from django.shortcuts import render, redirect

def forum_list(request):
    posts = [
        {"id": 1, "title": "How to reduce plastic use?", "author": "Aarav", "date": "2025-10-20", "content": "Let's share ideas on minimizing single-use plastic."},
        {"id": 2, "title": "Best eco-friendly travel tips?", "author": "Diya", "date": "2025-10-18", "content": "What are your favorite green travel hacks?"},
    ]
    return render(request, 'forum_list.html', {"posts": posts})


def forum_detail(request, post_id):
    sample_post = {
        "title": "How to reduce plastic use?",
        "author": "Aarav",
        "date": "2025-10-20",
        "content": "Let's share ideas on minimizing single-use plastic.",
    }
    comments = [
        {"author": "Diya", "text": "I’ve switched to metal straws and cloth bags!"},
        {"author": "Karan", "text": "Using refill stations helps a lot too."},
    ]
    return render(request, 'forum_detail.html', {"post": sample_post, "comments": comments})
