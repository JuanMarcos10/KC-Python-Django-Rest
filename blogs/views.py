from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog

def latest_blog(request):
    # Recuperamos los últimos posts de la base de datos
    blogs = Blog.objects.all().order_by('-creation_date')

    # Creamos el contexto para pasarle los post a la plantilla
    context = {'latest_blog': blogs}

    # Crear respuesta HTML con las posts
    html = render(request, 'latest.html', context)

    # Devolver la respuesta HTTP
    return HttpResponse(html)
