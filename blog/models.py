from datetime import datetime
from time import gmtime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from category.models import Category
import pytz

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    title = models.CharField(max_length=50, null=False, verbose_name='Título', unique=True)
    slug = models.SlugField(max_length=50, null=False, unique=True)
    theme = models.TextField(max_length=300, null=False, verbose_name='Breve descripción')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')
    description = models.TextField(null=False, verbose_name='Descripción')
    image_front = models.ImageField(upload_to='post/', blank=True, verbose_name='Imagen de portada')
    image = models.ImageField(upload_to='post/', blank=True, verbose_name='Imagen')
    is_activate = models.BooleanField(default=False, verbose_name=' Activo')
    activate_date = models.DateTimeField(verbose_name='Fecha de activación')
    due_date = models.DateTimeField(verbose_name='Fecha de caducidad')
    create_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        pacific = pytz.timezone('America/Bogota')
        date_init = int(self.activate_date.strftime('%Y%m%d%H%M%S'))
        date_end = int(self.due_date.strftime('%Y%m%d%H%M%S'))
        date_now = int(datetime.now(pacific).strftime('%Y%m%d%H%M%S'))

        if date_init  <= date_now  and date_now < date_end:
            self.is_activate = True
        else:
            self.is_activate = False
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Publicación')
    content = models.TextField(verbose_name='Contenido', null=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Publicación')
    like = models.BooleanField(default=True, verbose_name='Me gusta')
