from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('CLOTHING', 'Clothing'),
        ('BOOKS', 'Books'),
        # Add more choices as needed
    ]
    title = models.CharField(max_length = 20)
    category = models.CharField(max_length = 20,choices = CATEGORY_CHOICES,)
    desc = models.TextField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title
