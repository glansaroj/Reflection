from django.db import models


# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=20)
    notes = models.TextField()
    image = models.ImageField(upload_to='notes', blank=True, null=True)
    created_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"
