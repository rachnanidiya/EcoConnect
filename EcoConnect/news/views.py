from django.shortcuts import render

# Create your views here.
app_name = "news"
def news_list(request):
    news_articles = [
        {
            'id': 1,
            'title': 'Local Tree Plantation Drive Achieves Record Participation',
            'description': 'Over 500 volunteers joined the city-wide initiative to plant 2,000 trees in one day.',
            'image': "images/treeplat.jpg",
            'date': 'October 20, 2025',
        },
        {
            'id': 2,
            'title': 'Ban on Single-use Plastics Takes Effect in Major Cities',
            'description': 'The new regulation aims to reduce plastic waste and encourage sustainable alternatives.',
            'image': 'images/noplastic.jpg',
            'date': 'October 27, 2025',
        },
         {
        'id': 3,
        'title': 'EcoConnect Youth Club Launches Clean Water Campaign',
        'description': 'Students across the city are participating in awareness activities on water conservation.',
        'image': 'images/water.jpg',
        'date': 'November 3, 2025',
    },
    {
        'id': 4,
        'title': 'Record Solar Power Generation Achieved This Month',
        'description': 'Solar farms reported a sharp rise in clean energy output due to improved panels.',
        'image': 'images/solar.jpg',
        'date': 'November 18, 2025',
    },
    {
        'id': 5,
        'title': 'Eco-Friendly Packaging Gains Popularity Among Local Stores',
        'description': 'More businesses are switching to biodegradable and compostable packaging materials.',
        'image': 'images/package.jpg',
        'date': 'November 25, 2025',
    },
    {
        'id': 6,
        'title': 'Urban Garden Project Helps Families Grow Their Own Food',
        'description': 'More than 100 families have started growing organic vegetables in shared community gardens.',
        'image': 'images/urban.jpg',
        'date': 'December 8, 2025',
    },
    ]
    return render(request, 'news_list.html', {'news_articles': news_articles})

def news_detail(request, id):
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
