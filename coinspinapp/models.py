from django.db import models
from firebase_admin import firestore
# Create your models here.
class Coinmaster(models.Model):
    detail = models.TextField()
    link = models.URLField()
    title = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'Coinmaster'
        
    def __str__(self) -> str:
        return self.link
  
class Post(models.Model):
    sno = models.CharField(max_length=255)
    Detail = models.TextField()
    Link = models.URLField()
    Title = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return self.Link
    
    
