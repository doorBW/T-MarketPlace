# Generated by Django 2.2.1 on 2019-11-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='photo',
            field=models.ImageField(default='markets.png', upload_to='images/'),
        ),
    ]