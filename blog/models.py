from django.db import models #ver en docs los tipos de field
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Modelos de Usuarios y posts

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #fecha actual
    author = models.ForeignKey(User, on_delete=models.CASCADE) #si el usuario es eliminado, se eliminaran sus posts

    def __str__(self): #devuelve title (revisar funciones especiales)
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        #indicamos que luego de crear un post redirijamos hacia la ruta de name post-detail y pasamos el parametro pk (ejm: /post/5, si el post que creamos es el 5o)