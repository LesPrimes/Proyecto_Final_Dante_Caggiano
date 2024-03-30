from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import *
from .formss import *

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


#____________Login, Logout, Authentication, Registration etc...


def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)




            #______ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #________________________________________________________

            return render(request, "App/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    
        miForm = AuthenticationForm()

    return render(request, "App/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        myForm = RegistroForm(request.POST)

        if myForm.is_valid():
            usuario = myForm.cleaned_data.get("username")
            myForm.save()
            return redirect(reverse_lazy('home'))
    else:
        myForm = RegistroForm()

    return render(request, "App/registration.html", {"form": myForm} )


#_______________Edicion de Perfil,Cambio de Clave, Avatar
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else: 
        miForm = UserEditForm(instance=usuario)

    return render(request, "App/profileEdit.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "App/changePassword.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)

            #____Borrador de avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #_______________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render(request, "App/agregarAvatar.html", {"form": miForm} )





#___________________________________________CRUDE
    

#________________________Pantalon
class PantalonList(LoginRequiredMixin,ListView):
    model = Pantalon

class PantalonCreate(LoginRequiredMixin,CreateView):
    model = Pantalon
    fields = ["nombre","precio","marca"]
    success_url = reverse_lazy("pantalones")

class PantalonUpdate(LoginRequiredMixin,UpdateView):
    model = Pantalon
    fields = ["nombre", "precio", "marca"]
    success_url = reverse_lazy("pantalones")

class PantalonDelete(LoginRequiredMixin,DeleteView):
    model = Pantalon
    success_url = reverse_lazy("pantalones") 



#________________________Zapatilla
class ZapatillaList(LoginRequiredMixin,ListView):
    model = Zapatilla

class ZapatillaCreate(LoginRequiredMixin,CreateView):
    model = Zapatilla
    fields = ["nombre", "precio", "marca"]
    success_url = reverse_lazy("zapatillas")

class ZapatillaUpdate(LoginRequiredMixin,UpdateView):
    model = Zapatilla
    fields = ["nombre", "precio", "marca"]
    success_url = reverse_lazy("zapatillas")

class ZapatillaDelete(LoginRequiredMixin,DeleteView):
    model = Zapatilla
    success_url = reverse_lazy("zapatillas") 



#________________________ Gorra
class GorraList(LoginRequiredMixin,ListView):
    model = Gorra

class GorraCreate(LoginRequiredMixin,CreateView):
    model = Gorra
    fields = ["nombre", "precio", "marca"]
    success_url = reverse_lazy("gorras")

class GorraUpdate(LoginRequiredMixin,UpdateView):
    model = Gorra
    fields = ["nombre", "precio", "marca"]
    success_url = reverse_lazy("gorras")

class GorraDelete(LoginRequiredMixin,DeleteView):
    model = Gorra
    success_url = reverse_lazy("gorras") 


#________________________Remera
class RemeraList(LoginRequiredMixin,ListView):
    model = Remera

class RemeraCreate(LoginRequiredMixin,CreateView):
    model = Remera
    fields = ["nombre", "precio", "marca"]
    success_url = reverse_lazy("remeras")

class RemeraUpdate(LoginRequiredMixin,UpdateView):
    model = Remera
    fields = ["nombre", "precio", "marca"]
    success_url = reverse_lazy("remeras")

class RemeraDelete(LoginRequiredMixin,DeleteView):
    model = Remera
    success_url = reverse_lazy("remeras") 


#Otras rutas


def home(request):
    return render( request , "App/index.html" )

def about_me(request):
    return render(request,"App/AboutMe.html")


def nexter_info(request):
    return render(request,"App/nexter_info.html")