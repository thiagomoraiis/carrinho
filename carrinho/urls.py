from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('carrinho/', carrinho, name='carrinho'),
    # path('adicionar_item/<int:id>/', adicionar_item, name='adicionar_item'),
    path('remover_item/<int:id>/', remover_item, name='remover_item'),
    path('efetuar_compra/<int:id>/', efetuar_compra, name='efetuar_compra'),
    path('historico_compras/', historico_compras, name='historico_compras'),
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
    path('produto/<int:id>/', produto, name='produto')
]