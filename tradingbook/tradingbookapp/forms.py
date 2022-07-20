from django import forms
from django.forms.widgets import NumberInput
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm #formulario de autenticacion 
from django.contrib.auth.models import User
from .models import Avatar,Tradeimagen


posiciones=(
    ("1","Long"),
    ("2","Short"),
    
)
class NuevoTrade(forms.Form):
    fecha = forms.DateTimeField(label="fecha ", required=True, widget=NumberInput(attrs={'type':'date'}))
    simbolo = forms.CharField(label="simbolo")
    posicion = forms.ChoiceField(label="posicion",choices=posiciones)
    entrada = forms.FloatField(label="Precio Entrada",)
    target = forms.FloatField(label="Target")
    stop = forms.FloatField(label="stop")
    tradeimagen = forms.ImageField(label="tradeimagen",required=False)
    

    

class NuevaTradingnote(forms.Form):
    fecha = forms.DateTimeField(label="fecha ", required=True, widget=NumberInput(attrs={'type':'date'}))
    simbolo = forms.CharField(label="simbolo")
    nota = forms.CharField(label="Nota",widget=forms.Textarea(attrs={"rows":5, "cols":30}))


class NuevoMercado(forms.Form):
    pais =forms.CharField(label="pais")
    simbolo = forms.CharField(label="simbolo")
    
    
class UserRegisterform(UserCreationForm):
    
    
    foto = forms.ImageField(required=False)
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput) # lacontrasena no se ve 
    password2: forms.CharField(label="Password",widget=forms.PasswordInput)
    
    first_name = forms.CharField(label='Nombre',required=False)
    last_name=forms.CharField(label='Apellido',required=False)
    
    
    class Meta:
        model = User 
        fields=['username','email','password1','password2','first_name','last_name']
        # help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Email")  
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput,required=False) # lacontrasena no se ve 
    password2: forms.CharField(label="Confirmar Password",widget=forms.PasswordInput,required=False)
    first_name = forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    
    
    
    class Meta:
        model = User
        fields = ["email",'password1','password2','first_name','last_name']
        
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="imagen",required=False)
    
    class Meta:
        model = Avatar
        fields = ["imagen"]
        
        