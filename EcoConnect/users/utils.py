from .models import CustomUser

def add_eco_points(user, points):
    """
    Increment the eco_points of a user by the given points.
    """
    if user.is_authenticated:
        user.eco_points += points
        user.save()
