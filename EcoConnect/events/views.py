from django.shortcuts import redirect, render, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required
from events.models import Participation

def event_list(request):
    events = Event.objects.all()
    print(events)  # see if any events are being fetched
    return render(request, "event_list.html", {"events": events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, "event_detail.html", {"event": event})

@login_required
def join_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    participation, created = Participation.objects.get_or_create(
        user=request.user,
        event=event
    )

    if created:
        request.user.eco_points += 10
        request.user.save()

    return redirect('events:event_list')
