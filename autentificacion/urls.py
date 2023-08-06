from django.urls import path
from .views import Registro, cerrar_sesion, logear

urlpatterns = [
    path('', Registro.as_view(), name="autentificacion"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('login/', logear, name="login"),
]

