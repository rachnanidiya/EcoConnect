from django.db import models
from initiatives.models import Initiative
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        'Event', null=True, blank=True, on_delete=models.CASCADE
    )
    initiative = models.ForeignKey(
        Initiative, null=True, blank=True, on_delete=models.CASCADE
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event', 'initiative')

    def __str__(self):
        return f"{self.user}"
