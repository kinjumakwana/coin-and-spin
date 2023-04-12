from django.db import models

# Create your models here.
class Coinmaster(models.Model):
    detail = models.TextField()
    link = models.URLField()
    title = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'Coinmaster'
        
    def __str__(self) -> str:
        return self.link
    