from django.db import models

# Create your models here.
class blogpost(models.Model):
    title=models.CharField(max_length=255)
    desc=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='blog',null=True)
    post_by=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title