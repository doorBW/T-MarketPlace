# Generated by Django 2.2.7 on 2019-11-09 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='System', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(
                    default='../media/images/markets.png', upload_to='images/')),
                ('address', models.CharField(max_length=1000)),
                ('url', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('open_day', models.CharField(default='알 수 없음', max_length=30)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('files', models.FileField(upload_to='files/')),
                ('upload_date', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='Date published')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=100)),
                ('pay', models.CharField(max_length=50)),
                ('host', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images/')),
                ('address', models.CharField(max_length=1000)),
                ('url', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('created_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('market', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Market')),
            ],
        ),
    ]
