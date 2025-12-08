from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Address

User = get_user_model()

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user,
        'eco_points': request.user.eco_points,
        'addresses': request.user.addresses.all(),
    })

@login_required
def add_address(request):
    if request.method == "POST":
        Address.objects.create(
            user=request.user,
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            house=request.POST['house'],
            street=request.POST['street'],
            city=request.POST['city'],
            state=request.POST['state'],
            pincode=request.POST['pincode'],
            is_default=request.POST.get('is_default', False)
        )
        messages.success(request, "Address added successfully.")
        return redirect('profile')

    return render(request, 'add_address.html')

@login_required
def edit_address(request, id):
    address = get_object_or_404(Address, id=id, user=request.user)

    if request.method == "POST":
        address.full_name = request.POST['full_name']
        address.phone = request.POST['phone']
        address.house = request.POST['house']
        address.street = request.POST['street']
        address.city = request.POST['city']
        address.state = request.POST['state']
        address.pincode = request.POST['pincode']
        address.is_default = request.POST.get('is_default', False)
        address.save()
        messages.success(request, "Address updated successfully.")
        return redirect('profile')

    return render(request, 'edit_address.html', {"address": address})

@login_required
def delete_address(request, id):
    address = get_object_or_404(Address, id=id, user=request.user)
    address.delete()
    messages.success(request, "Address deleted successfully.")
    return redirect('profile')
