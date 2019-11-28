from django.urls import path
from .views import UsuarioList, UsuarioDetail, CartaoList, CartaoDetail, ContaList, ContaDetail, \
    FaturaList, FaturaDetail, LancamentoList, LancamentoDetail


urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name=UsuarioList.name),
    path('usuarios/<int:id>/', UsuarioDetail.as_view(), name=UsuarioDetail.name),
    path('cartoes/', CartaoList.as_view(), name=CartaoList.name),
    path('cartoes/<int:id>/', CartaoDetail.as_view(), name=CartaoDetail.name),
    path('faturas/', FaturaList.as_view(), name=FaturaList.name),
    path('faturas/<int:id>/', UsuarioDetail.as_view(), name=UsuarioDetail.name),
    path('contas/', ContaList.as_view(), name=ContaList.name),
    path('contas/<int:id>/', ContaDetail.as_view(), name=ContaDetail.name),
    path('lancamentos/', LancamentoList.as_view(), name=LancamentoList.name),
    path('lancamentos/<int:id>/', LancamentoDetail.as_view(), name=LancamentoDetail.name),
]