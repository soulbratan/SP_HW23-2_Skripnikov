from django.db.models import BooleanField
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Product


BANNED_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар"
]

def validate_no_banned_words(value):
    """Проверяет отсутствие запрещённых слов (регистронезависимо)."""
    lower_value = value.lower()
    for word in BANNED_WORDS:
        if word in lower_value:
            raise ValidationError(f"Использование слова '{word}' запрещено!")

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
        validate_no_banned_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        validate_no_banned_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной!")
        return price

