from django.db import models
import datetime
from django.contrib.auth.models import User

#modelo del avatar 
class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/',blank=True,null=True)
# para  este modelo tuvimos que crear una carpeta media a nivel de manage.py y ademas registramos su URL en la carpeta setting 


class Trade(models.Model):
    fecha = models.DateField("Fecha de operacion (mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    simbolo = models.CharField("Simbolo",max_length=30)
    
    posiciones = (
        (1,"Long"),
        (2,"Short")
    )
    posicion = models.PositiveSmallIntegerField("Posicion",choices=posiciones)
    entrada = models.FloatField("Precio Entrada",)
    target = models.FloatField("Target")
    stop = models.FloatField("stop")
    tradeimagen = models.ImageField(upload_to='tradesimg',null=True)
    

class Note(models.Model):
    fecha = models.DateField("Fecha de operacion (mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    simbolo = models.CharField("Simbolo",max_length=30)
    nota = models.CharField("Notas de trading", max_length=250)
    
    
class  Market(models.Model):
    pais = models.CharField("pais a donde pertenece",max_length=30)
    simbolo = models.CharField("Simbolo a observar",max_length=30)
    


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    imagenavatar = models.ImageField(upload_to='avatar/',blank=True,null=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username
    
    
class Tradeimagen(models.Model): # esto no esta bien por que estoy relacionando con un usuario, asi se haria para mostrar solo lo que mostro ese usuraio 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) #pendiente!!!!!
    tradeimagen = models.ImageField(upload_to='tradesimagen/',blank=True,null=True)