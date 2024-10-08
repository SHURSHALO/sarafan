# Generated by Django 4.2.15 on 2024-08-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "products",
            "0003_alter_product_image_large_alter_product_image_medium_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image_large",
            field=models.ImageField(
                upload_to="post_images/large/",
                verbose_name="Изображение продукта 640 x 480.",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_medium",
            field=models.ImageField(
                upload_to="post_images/medium/",
                verbose_name="Изображение продукта 320 x 240.",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_small",
            field=models.ImageField(
                upload_to="post_images/small/",
                verbose_name="Изображение продукта 240 x 180.",
            ),
        ),
    ]
