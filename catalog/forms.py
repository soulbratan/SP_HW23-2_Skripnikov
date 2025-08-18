from django.forms import ModelForm

from catalog.models import Product, Category

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
