# Generated by Django 2.2 on 2020-01-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishes',
            options={'ordering': ('name',), 'verbose_name': 'Dishes', 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterField(
            model_name='dishes',
            name='image',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]
