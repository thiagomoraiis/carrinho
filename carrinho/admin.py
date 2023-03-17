from django.contrib import admin
from .models import *

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'quantidade_disponivel')

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('item', 'carrinho', 'quantidade')

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('status',)
