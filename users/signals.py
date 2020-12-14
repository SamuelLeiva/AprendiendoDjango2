#signal que es disparada despues que un objeto es guardado
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#objeto que recibira la signal y realizara una tarea
from django.dispatch import receiver
from .models import Profile

#funcion para crear un profile cada vez que un user es creado
#cuando un user es creado, envia la signal que es recibida por este receiver
#y esta funcion crea un profile si un user se ha creado
@receiver(post_save, sender=User) #(signal, sender)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#cuando un user sea guardado, guardara el profile
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()