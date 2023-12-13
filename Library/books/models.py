from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Authors'
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    published_date = models.DateField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'Books'
        unique_together = ['title', 'author']
    