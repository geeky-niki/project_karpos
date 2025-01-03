# Generated by Django 5.1.4 on 2024-12-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daily_transection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('cust_name', models.CharField(max_length=100)),
                ('product_bought', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField()),
                ('is_regular', models.BooleanField(default=False)),
            ],
        ),
    ]
