from django.shortcuts import render, get_object_or_404
from .models import Event

def event_list(request):
    events = Event.objects.all()
    print(events)  # see if any events are being fetched
    return render(request, "event_list.html", {"events": events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, "event_detail.html", {"event": event})
