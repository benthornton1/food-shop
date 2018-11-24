# Generated by Django 2.1.3 on 2018-11-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20181124_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='unit',
            field=models.CharField(choices=[('g', 'Grams'), ('single', 'Single'), ('kg', 'Kilograms'), ('ml', 'Milliliters'), ('l', 'Liters')], default='g', max_length=200),
        ),
    ]
