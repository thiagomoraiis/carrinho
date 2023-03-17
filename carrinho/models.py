from django.db import models

# Produto
class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade_disponivel = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

# Carrinho
class Carrinho(models.Model):
    status = models.CharField(max_length=20, choices=(('aberto', 'Aberto'), ('fechado', 'Fechado')))
    itens = models.ManyToManyField(Item, through='ItemCarrinho')

    def __str__(self):
        return f'{self.itens}'

# Carrinho Item
class ItemCarrinho(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField('',null=False)

    def __str__(self):
        return self.item