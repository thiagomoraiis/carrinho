from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Carrinho, ItemCarrinho
from .forms import ItemModelForm
from django.contrib import messages

def index(request):
    item = Item.objects.all()
    context = {
        'p':item
    }
    return render(request, 'index.html', context)

def produto(request, id):
    prod = get_object_or_404(Item, id=id)
    if request.method == 'POST':    
        carrinho, created = Carrinho.objects.get_or_create(status='aberto')
        item_carrinho, created = ItemCarrinho.objects.get_or_create(item=prod, carrinho=carrinho, defaults={'quantidade': 0})
        quant = int(request.POST.get('quant', 0))
        item_carrinho.quantidade += quant
        print(item_carrinho.quantidade)
        item_carrinho.save()
        prod.quantidade_disponivel -= quant
        print(prod.quantidade_disponivel)
        prod.save()
    context = {
        'prod':prod
    }
    return render(request, 'produto.html', context)

# def adicionar_item(request, id):
#     item = get_object_or_404(Item, id=id)
#     carrinho, created = Carrinho.objects.get_or_create(status='aberto')
#     item_carrinho, created = ItemCarrinho.objects.get_or_create(item=item, carrinho=carrinho, defaults={'quantidade': 0})
#     item_carrinho.quantidade += 1
#     item_carrinho.save()
#     item.quantidade_disponivel -= 1
#     item.save()
#     return redirect('carrinho')

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar o produto')
            form = ItemModelForm()
    else:
        form = ItemModelForm()
    context = {
        'form':form
    }
    return render(request, 'cadastrar_produto.html', context)

def carrinho(request):
    carrinho = Carrinho.objects.filter(status='aberto').first()
    itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
    context = {
        'carrinho': carrinho, 
        'itens_carrinho': itens_carrinho
    }
    return render(request, 'carrinho.html', context)

def remover_item(request, id):
    item = get_object_or_404(Item, id=id)
    carrinho = Carrinho.objects.filter(status='aberto').first()
    item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, item=item).first()
    if request.method == 'POST':
        item_carrinho.delete()
        item.quantidade_disponivel += 1
        print(item.quantidade_disponivel)
        item.save()
        return redirect('carrinho')
    context = {
        'item_carrinho': item_carrinho,
        'item':item
    }
    return render(request, 'remover_item.html', context)
    # return redirect('carrinho')

def efetuar_compra(request, id):
    car = get_object_or_404(Carrinho, id=id)
    carrinho = Carrinho.objects.filter(status='aberto').first()
    itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
    if request.method == 'POST':
        for item_carrinho in itens_carrinho:
            item = item_carrinho.item
            if item_carrinho.quantidade > item.quantidade_disponivel:
                return render(request, 'erro_compra.html')
            item.quantidade_disponivel -= item_carrinho.quantidade
            print(item.quantidade_disponivel)
            item.save()
        carrinho.status = 'fechado'
        carrinho.save()
        return redirect('home')
    context = {
        'carrinho':carrinho,
        'car':car
    }
    return render(request, 'efetuar_compra.html', context)
    # return redirect('historico_compras')

def historico_compras(request):
    carrinhos = Carrinho.objects.filter(status='fechado')
    context = {
        'carrinhos': carrinhos
    }
    return render(request, 'historico_compras.html', context)
