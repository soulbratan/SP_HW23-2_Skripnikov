from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        max_length=150,
        verbose_name="Описание категории",
        help_text="Описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
    )
    description = models.CharField(
        max_length=150, verbose_name="Описание", help_text="Описание товара"
    )
    photo = models.ImageField(
        upload_to="catalog/photos", verbose_name="Фотография", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Введите цену за покупку",
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "updated_at"]

    def __str__(self):
        return self.name

