from django.db.models import BooleanField
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Product


BANNED_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар"
]

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
        exclude = ("views_count",)

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for word in BANNED_WORDS:
            if word in name:
                raise ValidationError(f"Запрещено использовать слово: '{word}'!")
        return self.cleaned_data['name']

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        for word in BANNED_WORDS:
            if word in description:
                raise ValidationError(f"Запрещено использовать слово: '{word}'!")
        return self.cleaned_data['description']

