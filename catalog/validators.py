from django.core.exceptions import ValidationError

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