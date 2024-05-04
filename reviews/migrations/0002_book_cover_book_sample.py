# Generated by Django 5.0.3 on 2024-03-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='book_covers/', verbose_name="The book's cover"),
        ),
        migrations.AddField(
            model_name='book',
            name='sample',
            field=models.FileField(null=True, upload_to='book_samples/', verbose_name='Sample for the book'),
        ),
    ]
