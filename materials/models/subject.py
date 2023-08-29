from django.db import models

from materials.models import Course
from users.models import NULLABLE


class Subject(models.Model):
    title = models.CharField(unique=True, max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    preview = models.ImageField(upload_to='materials/subjects/preview', verbose_name='Превью', **NULLABLE)
    video_link = models.CharField(max_length=150, verbose_name="Ссылка на видео", **NULLABLE)

    course = models.ForeignKey(Course, verbose_name="курс", **NULLABLE, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
