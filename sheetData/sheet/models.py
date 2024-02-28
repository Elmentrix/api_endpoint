from django.db import models

# creating model to hold items, descriptions, and images
class items(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
