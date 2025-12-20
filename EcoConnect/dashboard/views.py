# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from events.models import Event, Participation
from initiatives.models import Initiative
from forum.models import ForumPost


@login_required
def user_dashboard(request):
    user = request.user

    joined_events = Event.objects.filter(
        id__in=Participation.objects.filter(user=user, event__isnull=False).values_list('event_id', flat=True)
    )

    joined_initiatives = Initiative.objects.filter(
        id__in=Participation.objects.filter(user=user, initiative__isnull=False).values_list('initiative_id', flat=True)
    )

 
    forum_posts = ForumPost.objects.filter(author=user)

   

    stats = {
        'events_count': joined_events.count(),
        'initiatives_count': joined_initiatives.count(),
        'forum_posts_count': forum_posts.count(),
      
    }

    context = {
        'user': user,
        'stats': stats,
        'joined_events': joined_events,
        'joined_initiatives': joined_initiatives,
        'forum_posts': forum_posts,
       
    }

    return render(request, 'user_dashboard.html', context)
