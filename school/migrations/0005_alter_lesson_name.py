# Generated by Django 4.1.7 on 2023-02-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_lesson_review_lesson_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='название'),
        ),
    ]
