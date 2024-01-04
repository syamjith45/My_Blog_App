from django.db import models

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=255,default='')
    short_desc=models.CharField(max_length=255,default='')
    id=models.AutoField(primary_key=True)
    content=models.TextField()
    thumbnail=models.ImageField(upload_to="blogimages")
    created_at=models.TimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title