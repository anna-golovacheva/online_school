from django.conf import settings
from django.db import models
from django.utils.text import slugify

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='превью')
    description = models.CharField(max_length=500, verbose_name='описание')
    author = models.ForeignKey(User, **NULLABLE, on_delete=models.CASCADE, verbose_name='автор')

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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.CASCADE, verbose_name='автор')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Payment(models.Model):
    CASH = 'cash'
    TRANSFER = 'trans'

    PAYMENT_CHOICES = [
        (CASH, 'наличные'),
        (TRANSFER, 'перевод')
    ]

    user = models.ForeignKey(User, **NULLABLE, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='оплаченный курс')
    lesson = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.CASCADE, verbose_name='оплаченный урок')
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method_of_payment = models.CharField(max_length=5, choices=PAYMENT_CHOICES, default=CASH, verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        if self.course:
            return f'{self.user} - {self.date} - {self.course}'
        return f'{self.user} - {self.date} - {self.lesson}'
