from curses.ascii import US
from django.contrib import admin
from aplicacion.models import Usuario, Tweet, Retweet

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tweet)
admin.site.register(Retweet)