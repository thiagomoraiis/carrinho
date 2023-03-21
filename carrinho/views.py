from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ItemModelForm
from django.contrib import messages
from django.views.generic import View,ListView, CreateView
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'p'
    model = Item

class DetalheProdutoView(View):
    def get(self, request, id):
        prod = get_object_or_404(Item, id=id)
        context = {'prod': prod}
        return render(request, 'produto.html', context)
    
    def post(self, request, id):
        prod = get_object_or_404(Item, id=id)
        carrinho, created = Carrinho.objects.get_or_create(status='aberto')
        item_carrinho, created = ItemCarrinho.objects.get_or_create(item=prod, carrinho=carrinho, defaults={'quantidade':0})
        quant = int(request.POST.get('quant', 0))
        item_carrinho.quantidade += quant
        item_carrinho.save()
        prod.quantidade_disponivel -= quant
        prod.save()
        context = {'prod':prod}
        return render(request, 'produto.html', context)
    

class ProdutoCreateView(CreateView):
    template_name = 'cadastrar_produto.html'
    model = Item
    fields = ('nome', 'descricao', 'preco', 'quantidade_disponivel')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar o produto')
        return super().form_invalid(form)
    

class CarrinhoListView(ListView):
    model = ItemCarrinho
    template_name = 'carrinho.html'
    context_object_name = 'itens_carrinho'

    def get_queryset(self):
        carrinho = Carrinho.objects.filter(status='aberto').first()
        queryset = super().get_queryset().filter(carrinho=carrinho)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrinho'] = Carrinho.objects.filter(status='aberto').first()
        return context


class RemoverItemView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        carrinho = Carrinho.objects.filter(status='aberto').first()
        item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, item=item).first()
        context = {
            'item_carrinho':item_carrinho,
            'item':item
        }
        return render(request, 'remover_item.html', context)
    
    def post(self, request,id):
        item = get_object_or_404(Item, id=id)
        carrinho = Carrinho.objects.filter(status='aberto').first()
        item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, item=item).first()
        item_carrinho.delete()
        item.quantidade_disponivel += 1
        item.save()
        return redirect('carrinho')


class EfetuarCompraView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        carrinho = Carrinho.objects.filter(status='aberto').first()
        item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, item=item).first()
        context = {
            'carrinho':carrinho,
            'car':item_carrinho,
        }
        return render(request, 'efetuar_compra.html', context)

    def post(self, request, id):
        item = get_object_or_404(Item, id=id)
        carrinho = Carrinho.objects.filter(status='aberto').first()
        item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, item=item).first()
        quantidade_item = item_carrinho.quantidade
        item_carrinho.delete()
        item.quantidade_disponivel -= quantidade_item
        item.save()
        return redirect('historico_compras')


class HistoricoComprasListView(ListView):
    model = Carrinho
    queryset = Carrinho.objects.filter(status='fechado')
    template_name = 'historico_compras.html'
    context_object_name = 'carrinhos'