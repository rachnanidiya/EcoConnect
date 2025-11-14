from django.shortcuts import render

# Create your views here.
def initiatives_list(request):

    initiatives = [
        {'id': 1, 'title': 'Tree Plantation Drive', 'location': 'Delhi', 'date': '2025-11-10', 'image': 'images/tree.jpg'},
        {'id': 2, 'title': 'Plastic-Free Week', 'location': 'Mumbai', 'date': '2025-11-15', 'image': 'images/nop2.jpg'},
        {'id': 3, 'title': 'Beach Cleanup', 'location': 'Goa', 'date': '2025-11-20', 'image': 'images/beach2.jpg'},
    ]
    return render(request, 'initiatives_list.html', {'initiatives': initiatives})

def initiative_detail(request, id):
    initiative = {
        'title': 'Tree Plantation Drive',
        'location': 'Delhi',
        'date': '2025-11-10',
        'description': 'Join our tree plantation drive to make the city greener!',
        'image': 'images/tree.jpg',
        'organizer': 'EcoConnect Team',
    }
    return render(request, 'initiative_detail.html', {'initiative': initiative})
