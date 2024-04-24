from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=20)
    notes = models.TextField()
    image = models.ImageField(upload_to='notes', blank=True, null=True)
    created_date = models.DateTimeField()
    owner = models.ForeignKey(
        User,  on_delete=models.CASCADE, related_name='journals', null=True)

    def __str__(self):
        return f"{self.title} | {self.created_date}"
