from rest_framework import serializers
from .models import Usuario, Cartao, Conta, Fatura, Lancamento


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['is_admin', 'is_active', 'is_staff']


class CartaoSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(many=False, queryset=Usuario.objects.all(), slug_field='nome')

    class Meta:
        model = Cartao
        fields = ['id', 'tipo', 'limite', 'conta', 'dia_encerramento_fatura', 'dia_vencimento_fatura', 'bandeira', 'numero', 'usuario']


class ContaSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(many=False, queryset=Usuario.objects.all(), slug_field='nome')

    class Meta:
        model = Conta
        fields = ['id', 'nome', 'saldo', 'tipo', 'instituicao', 'usuario']


class LancamentoSerializer(serializers.ModelSerializer):
    cartao = serializers.SlugRelatedField(many=False, queryset=Cartao.objects.all(), slug_field='numero')
    conta = serializers.SlugRelatedField(many=False, queryset=Cartao.objects.all(), slug_field='nome')

    class Meta:
        model = Lancamento
        fields = ['id', 'cartao', 'conta', 'fatura', 'descricao', 'categoria', 'data', 'valor']


class FaturaSerializer(serializers.ModelSerializer):
    cartao = serializers.SlugRelatedField(many=False, queryset=Cartao.objects.all(), slug_field='numero')
    
    class Meta:
        model = Fatura
        fields = ['id', 'referencia', 'valor', 'cartao']
