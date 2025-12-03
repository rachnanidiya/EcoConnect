from django.shortcuts import render

# Create your views here.
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
        {
        'id': 3,
        'title': 'Beach Restoration Campaign',
        'date': 'November 20, 2025',
        'location': 'Blue Coast Beach',
        'description': 'Help restore marine habitats by removing waste and planting dune grass.',
        'image': 'images/event3.jpg'
        },
    {
        'id': 4,
        'title': 'Eco-Friendly Market Festival',
        'date': 'December 1, 2025',
        'location': 'Green Square',
        'description': 'A marketplace promoting organic produce, handmade crafts, and sustainable brands.',
        'image': 'images/event4.jpg'
        },
    {
        'id': 5,
        'title': 'Recycling Awareness Marathon',
        'date': 'December 10, 2025',
        'location': 'City Stadium',
        'description': 'Run for the planet! A marathon dedicated to promoting recycling habits.',
        'image': 'images/event5.jpg'
    },
    {
        'id': 6,
        'title': 'Solar Energy Expo 2025',
        'date': 'December 18, 2025',
        'location': 'Expo Convention Center',
        'description': 'Explore the latest innovations in solar power and meet green tech companies.',
        'image': 'images/event6.jpg'
    },
    {
        'id': 7,
        'title': 'EcoConnect Club Meetup',
        'date': 'January 8, 2026',
        'location': 'EcoConnect HQ',
        'description': 'Networking meetup for all EcoConnect members to discuss future initiatives.',
        'image': 'images/event7.jpg'
    },
    {
        'id': 8,
        'title': 'Urban Garden Planting Day',
        'date': 'January 22, 2026',
        'location': 'Riverside Community Garden',
        'description': 'Join the community in building a new urban garden space for local families.',
        'image': 'images/event8.jpg'
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
