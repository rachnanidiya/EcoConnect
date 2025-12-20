from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from events.models import Participation
from .models import Initiative


def initiatives_list(request):
    initiatives = Initiative.objects.all().order_by('-date')
    return render(request, 'initiatives_list.html', {'initiatives': initiatives})

def initiative_detail(request, id):
    initiative = get_object_or_404(Initiative, id=id)
    joined_initiative_ids = Participation.objects.filter(
        user=request.user,
        initiative__isnull=False
    ).values_list('initiative_id', flat=True)
    return render(request, 'initiative_detail.html', {'initiative': initiative,'joined_initiative_ids': list(joined_initiative_ids),})

@login_required
def join_initiative(request, initiative_id):
    initiative = get_object_or_404(Initiative, id=initiative_id)

    participation, created = Participation.objects.get_or_create(
        user=request.user,
        initiative=initiative
    )

    if created:
        request.user.eco_points += 10
        request.user.save()

    return redirect('initiatives_list')