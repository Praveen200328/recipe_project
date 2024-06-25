# Generated by Django 5.0.6 on 2024-06-13 20:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category_image', models.ImageField(upload_to='catagories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('price', models.IntegerField()),
                ('product_description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priducts', to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]