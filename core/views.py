from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Usuario, Conta, Cartao, Fatura, Lancamento
from .serializers import UsuarioSerializer, ContaSerializer, CartaoSerializer, FaturaSerializer, LancamentoSerializer


class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    name = 'usuario-list'

    def post(self, request):
        try:
            user = Usuario.objects.create(nome=request.data['nome'], genero=request.data['genero'], email=request.data['email'])
        
            user.set_password(request.data['password'])
            user.save()

            return Response({'Message' : 'Usuário cadastrado!'}, status=status.HTTP_201_CREATED)
            
        except Exception:
            return Response({'Message' : 'Erro ao cadastrar usuário!'}, status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    name = 'usuario-detail'


class ContaList(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    name = 'conta-list'


class ContaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    name = 'conta-detail'


class CartaoList(generics.ListCreateAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
    name = 'cartao-list'


class CartaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
    name = 'cartao-detail'


class FaturaList(generics.ListCreateAPIView):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer
    name = 'fatura-list'


class FaturaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer
    name = 'fatura-detail'


class LancamentoList(generics.ListCreateAPIView):
    queryset = Lancamento.objects.all()
    serializer_class = LancamentoSerializer
    name = 'lancamento-list'


class LancamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lancamento.objects.all()
    serializer_class = LancamentoSerializer
    name = 'lancamento-detail'
