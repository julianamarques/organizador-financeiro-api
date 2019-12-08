from rest_framework import serializers
from .models import Usuario, Cartao, Conta, Fatura, Lancamento


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['is_admin', 'is_active', 'is_staff', 'saldo']


class CartaoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(many=False, queryset=Usuario.objects.all(), slug_field='nome')

    class Meta:
        model = Cartao
        fields = ['id', 'tipo', 'limite', 'conta', 'dia_encerramento_fatura', 'dia_vencimento_fatura', 'bandeira', 'numero', 'usuario']


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(many=False, queryset=Usuario.objects.all(), slug_field='nome')

    class Meta:
        model = Conta
        fields = ['id', 'nome', 'saldo', 'tipo', 'instituicao', 'usuario']


class LancamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lancamento
        fields = ['id', 'cartao', 'referencia', 'valor']


class FaturaSerializer(serializers.HyperlinkedModelSerializer):
    cartao = serializers.SlugRelatedField(many=False, queryset=Usuario.objects.all(), slug_field='bandeira')
    
    class Meta:
        model = Fatura
        fields = ['id', 'referencia', 'valor' 'cartao']
