from django.db import models
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='превью')
    description = models.CharField(max_length=500, verbose_name='описание')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', unique=True)
    preview = models.ImageField(upload_to='lessons/', **NULLABLE, verbose_name='превью')
    description = models.CharField(max_length=500, verbose_name='описание')
    slug = models.SlugField(max_length=50,  **NULLABLE, verbose_name='ссылка на урок')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='курс')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
