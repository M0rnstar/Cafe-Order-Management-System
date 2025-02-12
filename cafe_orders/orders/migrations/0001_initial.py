# Generated by Django 5.1.6 on 2025-02-08 14:17

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("table_number", models.IntegerField(verbose_name="Номер стола")),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=10,
                        verbose_name="Общая стоимость",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("waiting", "В ожидании"),
                            ("ready", "Готово"),
                            ("paid", "Оплачено"),
                        ],
                        default="waiting",
                        max_length=10,
                        verbose_name="Статус",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                    "dish_name",
                    models.CharField(max_length=100, verbose_name="Название блюда"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Цена"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.order",
                        verbose_name="Заказ",
                    ),
                ),
            ],
        ),
    ]
