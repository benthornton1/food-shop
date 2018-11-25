# Generated by Django 2.1.3 on 2018-11-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20181125_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.CharField(choices=[('m', 'Meat'), ('d', 'Dairy'), ('b', 'Baking'), ('p', 'Poultry')], default='m', max_length=200),
        ),
    ]
