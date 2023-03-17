from django import forms
from .models import Item, ItemCarrinho, Carrinho

class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'