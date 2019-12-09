from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


GENERO = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

TIPO_CONTA = [
    ('P', 'Poupança'),
    ('CC', 'Corrente'),
    ('C', 'Carteira'),
]

TIPO_CARTAO = [
    ('D', 'Débito'),
    ('C', 'Crédito'),
]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password):
        if not email:
            raise ValueError('O usuário deve possuir um email válido!')

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nome, password):
        user = self.create_user(
            email=email,
            nome=nome,
            password=password
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=1, choices=GENERO)
    email = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    @property
    def get_saldo_geral(self):
        contas = Conta.objects.filter(usuario=self)
        saldo = 0.0

        for conta in contas:
            saldo += conta.saldo

        return saldo

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super(Usuario, self).save()


class Conta(models.Model):
    nome = models.CharField(max_length=100)
    saldo = models.FloatField()
    tipo = models.CharField(max_length=2, choices=TIPO_CONTA)
    instituicao = models.CharField(max_length=100, blank=True)
    usuario = models.ForeignKey(Usuario,on_delete = models.CASCADE)

    def __str__(self):
        return self.nome


class Cartao(models.Model):
    tipo = models.CharField(max_length=1,choices=TIPO_CARTAO)
    limite = models.FloatField()
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    dia_encerramento_fatura = models.PositiveSmallIntegerField()
    dia_vencimento_fatura = models.PositiveSmallIntegerField()
    bandeira = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    numero = models.IntegerField()

    def __str__(self):
        return str(self.numero)


class Fatura(models.Model):
    cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=200)
    valor = models.FloatField()

    def __str__(self):
        return str(self.referencia)


class Lancamento(models.Model):
    conta = models.ForeignKey(Conta, on_delete= models.CASCADE)
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE)
    valor = models.FloatField()
    descricao = models.CharField(max_length=300)
    categoria = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return str(self.data + " " + self.categoria)
