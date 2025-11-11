from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def news_list(request):
    news_articles = [
        {
            'id': 1,
            'title': 'Local Tree Plantation Drive Achieves Record Participation',
            'description': 'Over 500 volunteers joined the city-wide initiative to plant 2,000 trees in one day.',
            'image': 'images/news1.jpg',
            'date': 'October 20, 2025',
        },
        {
            'id': 2,
            'title': 'Ban on Single-use Plastics Takes Effect in Major Cities',
            'description': 'The new regulation aims to reduce plastic waste and encourage sustainable alternatives.',
            'image': 'images/news2.jpg',
            'date': 'October 27, 2025',
        },
    ]
    return render(request, 'news_list.html', {'news_articles': news_articles})

def news_detail(request, id):
    # Temporary static data (for demonstration)
    news_item = {
        'id': id,
        'title': 'Local Tree Plantation Drive Achieves Record Participation',
        'description': 'Over 500 volunteers joined the city-wide initiative to plant 2,000 trees in one day.',
        'content': '''The EcoConnect team, in collaboration with GreenRoots Foundation, 
                      successfully hosted the event in 10 localities. Citizens from all age groups participated, 
                      contributing to sustainable city development.''',
        'image': 'images/news1.jpg',
        'date': 'October 20, 2025',
    }
    return render(request, 'news_detail.html', {'news_item': news_item})
