from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_default_preco():
    return 0.00

def get_default_preco_com_aumento():
    preco_inicial = get_default_preco()
    aumento = preco_inicial * 0.10
    preco_com_aumento = preco_inicial + aumento
    return preco_com_aumento

 
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)      
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='usuario_fotos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

 
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()    
    preco = models.DecimalField(max_digits=15, decimal_places=2, default=get_default_preco) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='usuario_fotos/', null=True, blank=True)

    def __str__(self):
        return self.nome

    
class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    carrinho = models.ForeignKey('Carrinho', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produto} - {self.quantidade}"


class Carrinho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through=ItemCarrinho)

    def __str__(self):
        return str(self.usuario)

    
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    endereco_entrega = models.CharField(max_length=200)
    status = models.CharField(choices=(
        ('pendente', 'Pendente'),
        ('concluido', 'Concluído'),
    ), max_length=20)
    item_carrinho = models.ManyToManyField(ItemCarrinho)

    def __str__(self):
        return f"{self.usuario} - {self.status}"
    

class Pagamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(choices=(
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado')
    ), max_length=20)

    def __str__(self):
        return f"{self.usuario} - {self.produto} - {self.status}"


class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ))
    comentario = models.TextField()

    def __str__(self):
        return f"{self.produto} - {self.nota}"


class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario)

    
class Notificacao(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    conteudo = models.TextField()
    lida = models.BooleanField(default=False)

    
    def __str__(self):
        return f"{self.tipo} - {self.conteudo}"