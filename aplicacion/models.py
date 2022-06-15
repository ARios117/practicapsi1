
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):

    username = models.CharField(max_length=100)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Tweet(models.Model):

    texto = models.CharField(max_length=100)

    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='tweets')

    class Meta:
        ordering = ['texto']

    def __str__(self):
        return self.texto


class Retweet(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='retweets')

    tweet = models.ForeignKey(Tweet, on_delete=models.SET_NULL, null=True, related_name='retweets')

    class Meta:
        ordering = ['usuario']

    def __str__(self):
        return 'Retweet - %s, %s: %s' % (self.usuario, self.tweet, self.fechaRetweet)