from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog

def index_blog(request):
    # Recuperar las últimas fotos de la base de datos
    blogs = Blog.objects.all()

    # Creamos el contexto para pasarle las fotos a la plantilla
    context = {'index_blog': blogs}

    # Crear respuesta HTML con las fotos
    html = render(request, 'latest.html', context)

    # Devolver la respuesta HTTP
    return HttpResponse(html)
