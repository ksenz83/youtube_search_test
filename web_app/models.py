from django.db import models

# Create your models here.


class KeyWordsData(models.Model):
    key_word = models.CharField('Ключевое слово', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.key_word


class VideoData(models.Model):
    youtube_id = models.CharField('Youtube ID', max_length=64, blank=True, null=True)
    key_word = models.ForeignKey(KeyWordsData, on_delete=models.CASCADE,)
    title = models.CharField('Название ролика', max_length=256, blank=True, null=True)
    url = models.CharField('Ссылка на ролик', max_length=64, blank=True, null=True)
    published_at = models.DateTimeField('Время публикации', null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.youtube_id + ' ' + self.title


from .signals import *