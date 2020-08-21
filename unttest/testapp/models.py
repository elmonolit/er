from django.db import models
class Category(models.Model):
    name = models.CharField(max_length = 125)
    def __str__(self):
        return self.name
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name =models.CharField(max_length = 300)
    url = models.URLField()
    def __str__(self):
        return self.name
# Create your models here.
