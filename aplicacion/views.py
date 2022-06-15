from django.shortcuts import render
from django.views import generic
from .models import Usuario, Retweet, Tweet

# Create your views here.

def lista_usuarios(request):

    context_dict = {}

    try:
        context_dict['username'] = Usuario.objects.get(id=1002)
        
        context_dict['retweets'] = Retweet.objects.filter(tweet__usuario__id=1002)
        context_dict['error'] = None

    except BaseException:

        context_dict['error'] = "Usuario no encontrado."
        context_dict['tweets'] = None
        context_dict['retweets'] = None
        context_dict['username'] = None

    return render(request, 'aplicacion/usuario.html', context_dict)
