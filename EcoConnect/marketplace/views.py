from django.shortcuts import render

USER_ECOPOINTS = 120   # static for testing
DISCOUNT_PER_POINT = 1 # 1 point = ₹1 discount
PRODUCTS = [
    {
        'id': 1,
        'title': 'Organic Vegetables Pack',
        'price': '₹150',
        'image': 'images/veg.jpg',
        'description': 'A fresh pack of organic vegetables grown locally.'
    },
    {
        'id': 2,
        'title': 'Handmade Bamboo Basket',
        'price': '₹300',
        'image': 'images/basket.jpg',
        'description': 'Eco-friendly handmade bamboo basket crafted by artisans.'
    },
    {
        'id': 3,
        'title': 'Pure Honey (500ml)',
        'price': '₹450',
        'image': 'images/honey.jpg',
        'description': 'Pure and natural honey sourced from local farms.'
    },
]


def marketplace_home(request):
    return render(request, 'mhome.html')


def marketplace_products(request):
    return render(request, 'products.html', {'products': PRODUCTS})


def marketplace_product_detail(request, id):
    product = next((p for p in PRODUCTS if p['id'] == id), None)

    # Calculate price after discount
    original_price = int(product['price'].replace('₹', ''))
    max_discount = min(USER_ECOPOINTS, original_price)  # cannot exceed price
    final_price = original_price - max_discount

    return render(
        request,
        'product_detail.html',
        {
            'product': product,
            'original_price': original_price,
            'final_price': final_price,
            'points_used': max_discount,
            'user_points': USER_ECOPOINTS,
        }
    )



def marketplace_sell_item(request):
    return render(request, 'sell_item.html')
