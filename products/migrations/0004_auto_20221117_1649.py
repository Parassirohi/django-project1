# Generated by Django 2.0.7 on 2022-11-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221117_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(),
        ),
    ]