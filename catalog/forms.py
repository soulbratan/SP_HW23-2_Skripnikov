from django.db.models import BooleanField
from django.forms import ModelForm

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fold_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название товара'})
    #     self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание товара'})
    #     self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите стоимость товара'})
    #     self.fields['category'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['photo'].widget.attrs.update({'class': 'input-group'})
