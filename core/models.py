from django.db import models


GENERO = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

TIPO_CONTA = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

TIPO_CARTAO = [
    ('D', 'Débito'),
    ('C', 'Crédito'),
]

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=1, choices=GENERO)
    email = models.CharField(max_length=50)
    saldo = models.FloatField()
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    nome = models.CharField(max_length=100)
    saldo = models.FloatField()
    tipo = models.CharField(max_length=1, choices=TIPO_CONTA)
    instituicao = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario,on_delete = models.CASCADE)

    def __str__(self):
        return self.nome


class Cartao(models.Model):
    tipo = models.CharField(max_length=1,choices=TIPO_CARTAO)
    limite = models.FloatField()
    conta = models.ForeignKey(Conta,on_delete=models.CASCADE)
    data_encerramento_fatura = models.DateField()
    data_vencimento = models.DateField()
    bandeira = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    numero = models.IntegerField()

    def __str__(self):
        return self.numero


class Fatura(models.Model):
    cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=200)
    valor = models.FloatField()

    def __str__(self):
        return self.referencia


class Lancamento(models.Model):
    conta = models.ForeignKey(Conta, on_delete= models.CASCADE)
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE)
    valor = models.FloatField()
    descricao = models.CharField(max_length=300)
    categoria = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return self.data + " " + self.categoria
