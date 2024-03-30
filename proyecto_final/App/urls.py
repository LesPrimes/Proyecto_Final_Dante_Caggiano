from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView



urlpatterns = [

    #_________________Urls
    path("", home , name="home"),
    path("AboutMe/",about_me, name ="AboutMe"),
    path("nexter/",nexter_info,name="nexter"),





    #________________________Remera

    path("remeras/",RemeraList.as_view(), name= "remeras"),
    path("remerascreate",RemeraCreate.as_view(), name = "remerascreate"),
    path("remerasupdate/<int:pk>/",RemeraUpdate.as_view(), name = "remerasupdate"),
    path("remerasdelete/<int:pk>/",RemeraDelete.as_view(), name = "remerasdelete"),

    #________________________Zapatilla

    path("zapatillas/",ZapatillaList.as_view(), name= "zapatillas"),
    path("zapatillascreate",ZapatillaCreate.as_view(), name = "zapatillascreate"),
    path("zapatillasupdate/<int:pk>/",ZapatillaUpdate.as_view(), name = "zapatillasupdate"),
    path("zapatillasdelete/<int:pk>/",ZapatillaDelete.as_view(), name = "zapatillasdelete"),

    #________________________Pantalon

    path("pantalones/",PantalonList.as_view(), name= "pantalones"),
    path("pantalonescreate",PantalonCreate.as_view(), name = "pantalonescreate"),
    path("pantalonesupdate/<int:pk>/",PantalonUpdate.as_view(), name = "pantalonesupdate"),
    path("pantalonesdelete/<int:pk>/",PantalonDelete.as_view(), name = "pantalonesdelete"),

    #________________________Gorra

    path("gorras/",GorraList.as_view(), name= "gorras"),
    path("gorrascreate",GorraCreate.as_view(), name = "gorrascreate"),
    path("gorrasupdate/<int:pk>/",GorraUpdate.as_view(), name = "gorrasupdate"),
    path("gorrasdelete/<int:pk>/",GorraDelete.as_view(), name = "gorrasdelete"),

    #_______________________Login,Logout, Registration
    path("login/" , login_request, name = "login"),
    path("logout/" , LogoutView.as_view(template_name="App/logout.html"),name = "logout"),
    path("register/" , register , name = "register"),

    #____________________ Edit Profile , Password Change, Add Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


]
