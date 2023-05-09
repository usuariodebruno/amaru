from django.contrib import admin
from .models import * #IMPORTAR TODAS AS MODELS 


@admin.register(Usuario) 
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'endereco', 'telefone')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'data_publicacao')
    list_filter = ('categoria', 'preco')
    search_fields = ('nome', 'descricao')


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'endereco_entrega', 'status')
    list_filter = ('status',)
    search_fields = ('endereco_entrega',)


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'produto', 'valor', 'status')
    list_filter = ('status',)


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'nota', 'usuario', 'comentario')


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'conteudo', 'lida')
    list_filter = ('tipo', 'lida')