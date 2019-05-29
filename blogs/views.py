from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from blogs.forms import BlogForm
from blogs.models import Blog


class LatestBlogsView(View):
    def get(self, request):
        # Recuperamos los últimos posts de la base de datos
        blogs = Blog.objects.all().order_by('-creation_date').select_related('owner')

        # Creamos el contexto para pasarle los post a la plantilla
        context = {'latest_blog': blogs[:5]}

        # Crear respuesta HTML con las posts
        html = render(request, 'latest.html', context)

        # Devolver la respuesta HTTP
        return HttpResponse(html)


class BlogDetailView(View):
    def get(self, request, pk, owner):
        # Recuperar el blog seleccionado de la base de datos
        blogs = get_object_or_404(Blog.objects.select_related('owner'), pk=pk)
        owner = owner

        # Crear un contexto para pasar la información a la plantilla
        context = dict(owner=owner, blog=blogs)

        # Renderizar plantilla
        html = render(request, 'detail.html', context)

        # Devolver respuesta HTTP
        return HttpResponse(html)


class NewBlogView(LoginRequiredMixin, View):

    def get(self, request):
        form = BlogForm()
        context = {'form': form}
        return render(request, 'new-post.html', context)

    def post(self, request):
        blog = Blog()
        blog.owner = request.user
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Post creado correctamente con ID {0}'.format(new_blog.pk))
            form = BlogForm()
        context = {'form': form}
        return render(request, 'new-post.html', context)


class BlogListView(View):
    def get(self, request):
        # Recuperamos los últimos posts de la base de datos
        blogs = Blog.objects.all().order_by('-creation_date')

        # Creamos el contexto para pasarle los post a la plantilla
        context = {'latest_blog': blogs}

        # Crear respuesta HTML con las posts
        html = render(request, 'list.html', context)

        # Devolver la respuesta HTTP
        return HttpResponse(html)


class UserBlogView(View):
    def get(self, request, owner):
        # Recuperar el blog seleccionado de la base de datos
        blogs = Blog.objects.all().order_by('-creation_date')
        owner = owner

        # Crear un contexto para pasar la información a la plantilla
        context = dict(owner=owner, blog=blogs)

        # Renderizar plantilla
        html = render(request, 'latest.html', context)

        # Devolver respuesta HTTP
        return HttpResponse(html)

