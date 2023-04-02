# Generated by Django 4.1.7 on 2023-03-24 03:27

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
            name='CosmeticCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(max_length=10)),
                ('avgRating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numReviews', models.IntegerField(max_length=10)),
                ('ingredients', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
                ('description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosapp.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeName', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('products', models.ManyToManyField(to='cosapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=50)),
                ('cateName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosapp.productcategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='typeName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosapp.producttype'),
        ),
        migrations.CreateModel(
            name='CosmeticBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(max_length=50)),
                ('priceRange', models.CharField(max_length=30)),
                ('companyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosapp.cosmeticcompany')),
            ],
        ),
    ]