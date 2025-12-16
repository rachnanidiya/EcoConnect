from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    date = models.DateField()

    def __str__(self):
        return self.title