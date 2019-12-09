from rest_framework import serializers
from .models import Usuario, Cartao, Conta, Fatura, Lancamento


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['is_admin', 'is_active', 'is_staff']


class CartaoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(many=False, queryset=Usuario.objects.all(), slug_field='nome')

    class Meta:
        model = Cartao
        fields = ['id','url', 'tipo', 'limite', 'conta', 'dia_encerramento_fatura', 'dia_vencimento_fatura', 'bandeira', 'numero', 'usuario']


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(many=False, queryset=Usuario.objects.all(), slug_field='nome')

    class Meta:
        model = Conta
        fields = ['id','url','nome', 'saldo', 'tipo', 'instituicao', 'usuario']


class LancamentoSerializer(serializers.HyperlinkedModelSerializer):
    conta = serializers.SlugRelatedField(many=False, queryset=Conta.objects.all(), slug_field='nome')

    class Meta:
        model = Lancamento
        fields = ['id','url','conta', 'fatura', 'descricao', 'categoria', 'data', 'valor']


class FaturaSerializer(serializers.HyperlinkedModelSerializer):
    cartao = serializers.SlugRelatedField(many=False, queryset=Cartao.objects.all(), slug_field='numero')
    
    class Meta:
        model = Fatura
        fields = ['id','url','referencia', 'valor', 'cartao']
