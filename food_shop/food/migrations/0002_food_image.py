# Generated by Django 2.1.3 on 2018-11-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, upload_to='food/food_img'),
        ),
    ]
