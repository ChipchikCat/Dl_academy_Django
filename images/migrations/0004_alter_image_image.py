# Generated by Django 4.1.6 on 2023-04-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_image_alter_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]