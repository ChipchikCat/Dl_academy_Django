from django.core.exceptions import ValidationError
from django.db import models
from learning_logs.models import Entry


def restrict_amount(value):
    if Entry.objects.filter(images=value).count() >= 5:
        raise ValidationError('Добавлено максимальное количество картинок.')


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
        related_name='images',
        validators=(restrict_amount, )
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title

