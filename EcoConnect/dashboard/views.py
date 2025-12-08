from django.shortcuts import render, redirect

# -------------------------------
# Dashboard Home
# -------------------------------
def dashboard_home(request):
    stats = {
        'total_products': 12,
        'total_users': 50,
        'total_orders': 28,
        'total_complaints': 6,
    }
    return render(request, 'dashboard_home.html', {'stats': stats})


# -------------------------------
# PRODUCTS MANAGEMENT
# -------------------------------
def dashboard_products_list(request):
    products = [
        {'id': 1, 'name': 'Reusable Water Bottle', 'price': 299, 'stock': 50},
        {'id': 2, 'name': 'Eco Bamboo Brush', 'price': 149, 'stock': 120},
        {'id': 3, 'name': 'Organic Cotton Bag', 'price': 199, 'stock': 80},
    ]
    return render(request, 'products_list.html', {'products': products})


def dashboard_add_product(request):
    return render(request, 'add_product.html')


def dashboard_edit_product(request, product_id):
    product = {'id': product_id, 'name': 'Reusable Water Bottle', 'price': 299, 'stock': 50}
    return render(request, 'edit_product.html', {'product': product})


def dashboard_delete_product(request, product_id):
    return redirect('dashboard:products_list')


# -------------------------------
# USERS MANAGEMENT
# -------------------------------
def dashboard_users_list(request):
    users = [
        {'id': 1, 'username': 'john', 'email': 'john@example.com'},
        {'id': 2, 'username': 'riya', 'email': 'riya@example.com'},
    ]
    return render(request, 'users_list.html', {'users': users})


# -------------------------------
# ORDERS MANAGEMENT
# -------------------------------
def dashboard_orders_list(request):
    orders = [
        {'id': 1, 'user': 'john', 'product': 'Water Bottle', 'total': 299, 'status': 'Delivered'},
        {'id': 2, 'user': 'riya', 'product': 'Cotton Bag', 'total': 199, 'status': 'Pending'},
    ]
    return render(request, 'orders_list.html', {'orders': orders})


# -------------------------------
# COMPLAINTS MANAGEMENT
# -------------------------------
def dashboard_complaints_list(request):
    complaints = [
        {'id': 1, 'user': 'john', 'subject': 'Late Delivery', 'status': 'Pending'},
        {'id': 2, 'user': 'riya', 'subject': 'Damaged Product', 'status': 'Resolved'},
    ]
    return render(request, 'complaints_list.html', {'complaints': complaints})


# -------------------------------
# NEWS MANAGEMENT
# -------------------------------
def dashboard_news_list(request):
    news = [
        {'id': 1, 'title': 'Tree Program Launched'},
        {'id': 2, 'title': 'Plastic-Free City Movement'},
    ]
    return render(request, 'news_list.html', {'news': news})


def dashboard_add_news(request):
    return render(request, 'add_news.html')


def dashboard_edit_news(request, news_id):
    news = {'id': news_id, 'title': 'Tree Program Launched'}
    return render(request, 'edit_news.html', {'news': news})


def dashboard_delete_news(request, news_id):
    return redirect('dashboard:news_list')


# -------------------------------
# INITIATIVES MANAGEMENT
# -------------------------------
def dashboard_initiatives_list(request):
    initiatives = [
        {'id': 1, 'title': 'Beach Cleanup Drive'},
        {'id': 2, 'title': 'Tree Plantation'},
    ]
    return render(request, 'initiatives_list.html', {'initiatives': initiatives})


def dashboard_add_initiative(request):
    return render(request, 'add_initiative.html')


def dashboard_edit_initiative(request, init_id):
    initiative = {'id': init_id, 'title': 'Beach Cleanup Drive'}
    return render(request, 'edit_initiative.html', {'initiative': initiative})


def dashboard_delete_initiative(request, init_id):
    return redirect('dashboard:initiatives_list')


# -------------------------------
# FEEDBACK MANAGEMENT
# -------------------------------
def dashboard_feedback_list(request):
    feedback = [
        {'id': 1, 'user': 'john', 'message': 'Great website!'},
        {'id': 2, 'user': 'riya', 'message': 'Loved the eco products!'},
    ]
    return render(request, 'feedback_list.html', {'feedback': feedback})
