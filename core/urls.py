from django.urls import path
from .views import UsuarioList, UsuarioDetail


urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name=UsuarioList.name),
    path('usuarios/<int:id>/', UsuarioDetail.as_view(), name=UsuarioDetail.name),
]