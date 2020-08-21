from django.db import models
from django.template.defaultfilters import slugify
class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default = 0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

# Create your models here.
