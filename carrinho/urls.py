from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('carrinho/', CarrinhoListView.as_view(), name='carrinho'),
    # path('adicionar_item/<int:id>/', adicionar_item, name='adicionar_item'),
    path('remover_item/<int:id>/', RemoverItemView.as_view(), name='remover_item'),
    path('efetuar_compra/<int:id>/', EfetuarCompraView.as_view(), name='efetuar_compra'),
    path('historico_compras/', HistoricoComprasListView.as_view(), name='historico_compras'),
    path('cadastrar_produto/', ProdutoCreateView.as_view(), name='cadastrar_produto'),
    path('produto/<int:id>/', DetalheProdutoView.as_view(), name='produto')
]