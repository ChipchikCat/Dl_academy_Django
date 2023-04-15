# Generated by Django 4.1.6 on 2023-04-15 15:36

from django.db import migrations, models
import django.db.models.deletion
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='learning_logs.entry', validators=[images.models.restrict_amount])),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
