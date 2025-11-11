from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def event_list(request):
    events = [
        {
            'id': 1,
            'title': 'Green City Clean-Up Drive',
            'date': 'November 5, 2025',
            'location': 'Central Park',
            'description': 'Join hands to make our city greener and cleaner. All volunteers welcome!',
            'image': 'images/event1.jpg'
        },
        {
            'id': 2,
            'title': 'Eco Workshop: Sustainable Living 101',
            'date': 'November 12, 2025',
            'location': 'Community Hall',
            'description': 'Learn practical sustainability skills for everyday life.',
            'image': 'images/event2.jpg'
        },
    ]
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, id):
    event = {
        'id': id,
        'title': 'Green City Clean-Up Drive',
        'date': 'November 5, 2025',
        'location': 'Central Park',
        'description': 'Join hands to make our city greener and cleaner.',
        'details': '''This event focuses on cleaning up local parks and roadsides. 
                      Participants are encouraged to bring reusable gloves and 
                      bottles. Certificates will be provided to all volunteers.''',
        'image': 'images/event1.jpg'
    }
    return render(request, 'event_detail.html', {'event': event})
