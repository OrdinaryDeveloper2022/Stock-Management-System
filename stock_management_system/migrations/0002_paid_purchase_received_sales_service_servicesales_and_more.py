# Generated by Django 4.0.1 on 2023-12-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'paid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'purchase',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Received',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'received',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('subcategory', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service_sales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stock',
                'managed': False,
            },
        ),
    ]
