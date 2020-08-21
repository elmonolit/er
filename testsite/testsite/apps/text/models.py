from django.db import models

class Text(models.Model):
    text_name = models.CharField("Название текста", max_length = 200)
    text_body = models.TextField("Здесь текст")
    def __str__(self):
        return self.text_name

# Create your models here.
