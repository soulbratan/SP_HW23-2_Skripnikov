from django.db import models

from users.models import User


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
    )
    description = models.CharField(
        max_length=150,
        verbose_name="Описание",
    )
    photo = models.ImageField(
        upload_to="catalog/photos", verbose_name="Фотография", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберете категорию",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Цена за покупку",
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата обновления", auto_now=True)
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Отметьте для публикации",
        editable=True,
        choices=[(True, "Опубликовано"), (False, "Не опубликовано")],
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "updated_at"]
        permissions = [("can_unpublish_product", "Can unpublish product")]

    def __str__(self):
        return self.name
