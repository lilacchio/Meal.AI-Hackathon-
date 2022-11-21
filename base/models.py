from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    bmi = models.IntegerField()
    location = models.CharField(max_length=100)
    budget = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created']