# Generated by Django 4.2.15 on 2024-08-17 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Заголовок"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="post_images",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.",
                        unique=True,
                        verbose_name="Идентификатор",
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Заголовок"),
                ),
                (
                    "image_small",
                    models.ImageField(upload_to="products/small/"),
                ),
                (
                    "image_medium",
                    models.ImageField(upload_to="products/medium/"),
                ),
                (
                    "image_large",
                    models.ImageField(upload_to="products/large/"),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.",
                        unique=True,
                        verbose_name="Идентификатор",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="Цена")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="products.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="Subcategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Заголовок"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="post_images",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.",
                        unique=True,
                        verbose_name="Идентификатор",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subcategories",
                        to="products.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "подкатегория",
                "verbose_name_plural": "Подкатегории",
            },
        ),
        migrations.CreateModel(
            name="Shopping",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Количество"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shopping_items",
                        to="products.product",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shopping",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Позиция в корзине",
                "verbose_name_plural": "Позиции в корзине",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="products.subcategory",
                verbose_name="Подкатегория",
            ),
        ),
    ]
