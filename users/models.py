from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here. 
class Profile(models.Model):
    #a cada user le corresponde uno y solo un profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) #si eliminamos un usuario se eliminan los profiles
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self): #si mandamos a imprimir este model que se muestre lo siguiente
        return f'{self.user.username} Profile'

    """def save(self, *args, **kwargs): #resize images
        super().save(*args, **kwargs) #metodo save de la clase padre

        img = Image.open(self.image.path) #image de la instancia actual

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)"""