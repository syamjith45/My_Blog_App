from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=255,default='')
    short_desc=models.CharField(max_length=255,default='')
    id=models.AutoField(primary_key=True)
    content=RichTextField()
    thumbnail=models.ImageField(upload_to="blogimages")
    created_at=models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    name=models.CharField(max_length=100,default="")
    blogparent=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Reply(models.Model):
    name=models.CharField(max_length=100,default="")
    commentparent = models.ForeignKey(Comment,on_delete=models.CASCADE)
    reply=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name