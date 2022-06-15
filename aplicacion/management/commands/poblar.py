# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data
# (https://zetcode.com/python/faker/)
import os

from django.core.management.base import BaseCommand
from aplicacion.models import (Usuario, Tweet, Retweet)
# from django.contrib.auth.models import User
from faker import Faker
# define STATIC_PATH in settings.py
# from proyecto.settings import STATIC_PATH
# from PIL import Image, ImageDraw, ImageFont
# from django.contrib.auth.hashers import make_password
from django.utils.dateparse import parse_date


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#


class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    # def add_arguments(self, parser):

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here
        if 'DYNO' in os.environ:
            self.font = \
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            self.font = \
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

        self.cleanDataBase()   # clean database
        self.usuario()
        self.tweet()
        self.retweet()
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here

    def cleanDataBase(self):
        Usuario.objects.all().delete()
        Tweet.objects.all().delete()
        Retweet.objects.all().delete()

    def usuario(self):

        usuario = {}

        usuario[1] = {'id': 1001,
                    'username': 'usuario_01',}
        usuario[2] = {'id': 1002,
                    'username': 'usuario_02',}
        usuario[3] = {'id': 1003,
                    'username': 'usuario_03',}

        for index, a in enumerate(usuario.values()):
            x = Usuario.objects.get_or_create(
                id=a['id'],
                username=a['username']
            )[0]
            x.save()

    def tweet(self):

        tweet = {}

        tweet[1] = {'id': 1001,
                      'texto': 'texto de mensaje 01',
                      'usuario': 1002,}
        tweet[2] = {'id': 1002,
                      'texto': 'texto de mensaje 02',
                      'usuario': 1001,}
        tweet[3] = {'id': 1003,
                      'texto': 'texto de mensaje 03',
                      'usuario': 1002,}
        tweet[4] = {'id': 1004,
                      'texto': 'texto de mensaje 04',
                      'usuario': 1002,}

        for index, a in enumerate(tweet.values()):
            x = Tweet.objects.get_or_create(
                id=a['id'],
                texto=a['texto'],
                usuario=Usuario.objects.get(id=int(a['usuario'])),
            )[0]
            x.save()

    def retweet(self):

        retweet = {}

        retweet[1] = {'id': 1001,
                      'tweet': 1001,
                      'usuario': 1003,}
        retweet[2] = {'id': 1002,
                      'tweet': 1001,
                      'usuario': 1001,}
        retweet[3] = {'id': 1003,
                      'tweet': 1002,
                      'usuario': 1003,}
        retweet[4] = {'id': 1004,
                      'tweet': 1003,
                      'usuario': 1003,}

        for index, a in enumerate(retweet.values()):
            x = Retweet.objects.get_or_create(
                id=a['id'],
                usuario=Usuario.objects.get(id=int(a['usuario'])),
                tweet=Tweet.objects.get(id=int(a['tweet'])),
            )[0]
            x.save()