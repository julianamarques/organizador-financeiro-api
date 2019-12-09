from django.urls import path
from django.views.generic import TemplateView
from .views import UsuarioList, UsuarioDetail, CartaoList, CartaoDetail, ContaList, ContaDetail, \
    FaturaList, FaturaDetail, LancamentoList, LancamentoDetail

from django.conf.urls.static import static
from configs import settings

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name=UsuarioList.name),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name=UsuarioDetail.name),
    path('cartoes/', CartaoList.as_view(), name=CartaoList.name),
    path('cartoes/<int:pk>/', CartaoDetail.as_view(), name=CartaoDetail.name),
    path('faturas/', FaturaList.as_view(), name=FaturaList.name),
    path('faturas/<int:pk>/', UsuarioDetail.as_view(), name=UsuarioDetail.name),
    path('contas/', ContaList.as_view(), name=ContaList.name),
    path('contas/<int:pk>/', ContaDetail.as_view(), name=ContaDetail.name),
    path('lancamentos/', LancamentoList.as_view(), name=LancamentoList.name),
    path('lancamentos/<int:pk>/', LancamentoDetail.as_view(), name=LancamentoDetail.name),
    path('openapi/', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL)