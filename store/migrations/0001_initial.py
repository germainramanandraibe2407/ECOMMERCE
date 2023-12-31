# Generated by Django 4.1.1 on 2022-09-07 08:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('commercial_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone_siege', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('num_fiscal', models.CharField(max_length=10)),
                ('num_stat', models.CharField(max_length=10)),
                ('num_cin', models.CharField(max_length=10)),
                ('nom_pers', models.CharField(max_length=100)),
                ('phone_pers', models.CharField(max_length=10)),
                ('email_pers', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('commercial_name', models.CharField(max_length=100)),
                ('marque_deposer', models.CharField(max_length=100, null=True)),
                ('marque_representer', models.CharField(max_length=100, null=True)),
                ('address', models.TextField()),
                ('phone_siege', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('num_fiscal', models.CharField(max_length=10)),
                ('num_stat', models.CharField(max_length=10)),
                ('num_cin', models.CharField(max_length=10)),
                ('nom_pers', models.CharField(max_length=100)),
                ('phone_pers', models.CharField(max_length=10)),
                ('email_pers', models.CharField(max_length=100)),
                ('liste_pays', models.CharField(max_length=100)),
                ('liste_fournisseur', models.CharField(max_length=100)),
                ('article_phare', models.CharField(max_length=100)),
                ('secteur_activite', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.products')),
            ],
        ),
    ]
