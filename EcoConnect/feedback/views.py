from django.shortcuts import render, redirect

def feedback(request):
    if request.method == 'POST':
        # You could print or just redirect to success
        return redirect('feedback_success')
    return render(request, 'feedback.html')

def feedback_success(request):
    return render(request, 'feedback_success.html')
