from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Usuario
from .serializers import UsuarioSerializer


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
