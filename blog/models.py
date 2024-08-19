from django.db import models

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    


