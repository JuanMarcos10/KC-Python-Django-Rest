from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from blogs.models import Blog

def latest_blog(request):
    # Recuperamos los últimos posts de la base de datos
    blogs = Blog.objects.all().order_by('-creation_date')

    # Creamos el contexto para pasarle los post a la plantilla
    context = {'latest_blog': blogs[:5]}

    # Crear respuesta HTML con las posts
    html = render(request, 'latest.html', context)

    # Devolver la respuesta HTTP
    return HttpResponse(html)


def blog_detail(request, pk):
    # Recuperar el blog seleccionado de la base de datos
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponseNotFound('Post Blog does not exist')

    # Crear un contexto para pasar la información a la plantilla
    context = {'blog': blog}

    # Renderizar plantilla
    html = render(request, 'detail.html', context)

    # Devolver respuesta HTTP
    return HttpResponse(html)
