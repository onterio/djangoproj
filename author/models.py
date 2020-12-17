# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField("Имя",max_length=100)
    age = models.PositiveSmallIntegerField("Возраст",default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="authors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Авторы"
        verbose_name_plural = "Авторы"