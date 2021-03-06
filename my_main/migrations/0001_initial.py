# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-14 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('ConsumeNum', models.IntegerField(primary_key=True, serialize=False)),
                ('ConsumeType', models.CharField(choices=[('movie', '电影'), ('products', '商品')], max_length=10)),
                ('ConsumeAmount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CusNum', models.IntegerField(primary_key=True, serialize=False)),
                ('CusName', models.CharField(max_length=10)),
                ('CusSex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmploeeNum', models.IntegerField(primary_key=True, serialize=False)),
                ('EmploeeName', models.CharField(max_length=10)),
                ('EmploeeSex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=5)),
                ('EmploeeDuty', models.CharField(choices=[('movieServer', '电影院服务员'), ('storeServer', '商店服务员'), ('movieAdmin', '电影院管理员'), ('storeAdmin', '商店管理员')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('GoodsNum', models.IntegerField(primary_key=True, serialize=False)),
                ('GoodsName', models.CharField(max_length=50)),
                ('GoodsPrice', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('MovieNum', models.IntegerField(primary_key=True, serialize=False)),
                ('MovieName', models.CharField(max_length=50)),
                ('MovieRank', models.IntegerField()),
                ('MovieProductor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MovieHouse',
            fields=[
                ('HouseNum', models.IntegerField(primary_key=True, serialize=False)),
                ('HousePlace', models.CharField(max_length=50)),
                ('HouseName', models.CharField(max_length=20)),
                ('HouseEmployee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='MovieSeat',
            fields=[
                ('SeatNum', models.IntegerField(primary_key=True, serialize=False)),
                ('SeatRow', models.IntegerField()),
                ('SeatLine', models.IntegerField()),
                ('SeatCustomer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='my_main.Customer')),
                ('SeatHouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.MovieHouse')),
            ],
        ),
        migrations.CreateModel(
            name='MovieSupplier',
            fields=[
                ('SupplierNum', models.IntegerField(primary_key=True, serialize=False)),
                ('SupplierName', models.CharField(max_length=50)),
                ('SupplierConnect', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('StoreNum', models.IntegerField(primary_key=True, serialize=False)),
                ('StoreName', models.CharField(max_length=20)),
                ('StorePlace', models.CharField(max_length=50)),
                ('StoreEmployee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('SupplierNum', models.IntegerField(primary_key=True, serialize=False)),
                ('SupplierName', models.CharField(max_length=20)),
                ('SupplierConnect', models.CharField(max_length=100)),
                ('SupplyConsume', models.ManyToManyField(to='my_main.Store')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='MovieHouse',
            field=models.ManyToManyField(to='my_main.MovieHouse'),
        ),
        migrations.AddField(
            model_name='movie',
            name='MovieSupp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.MovieSupplier'),
        ),
        migrations.AddField(
            model_name='goods',
            name='GoodsStore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.Store'),
        ),
        migrations.AddField(
            model_name='goods',
            name='GoodsSupplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.Supplier'),
        ),
        migrations.AddField(
            model_name='consume',
            name='Consumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.Customer'),
        ),
    ]
