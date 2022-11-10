from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Surl(models.Model):
    url = models.URLField()
    short = models.CharField(max_length=8)
    visit_count = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.url} - {self.short}"
