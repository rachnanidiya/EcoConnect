from django.db import models

# Create your models here.

class Initiative(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    date = models.DateField()
    description = models.TextField()
    organizer = models.CharField(max_length=150)
    image = models.ImageField(upload_to='initiatives/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
