from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title