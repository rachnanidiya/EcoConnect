from django.shortcuts import render, redirect
from .models import Feedback

def feedback(request):
    if request.method == "POST":
        Feedback.objects.create(
            user=request.user if request.user.is_authenticated else None,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return redirect('feedback_success')

    return render(request, 'feedback.html')

def feedback_success(request):
    return render(request, 'feedback_success.html')
