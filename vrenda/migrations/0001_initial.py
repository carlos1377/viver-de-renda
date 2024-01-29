# Generated by Django 5.0.1 on 2024-01-29 22:17

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FlowType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('clasification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vrenda.classification')),
                ('type_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vrenda.flowtype')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2024, 1, 29, 22, 17, 48, 408562, tzinfo=datetime.timezone.utc))),
                ('value', models.FloatField()),
                ('observation', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vrenda.flow')),
            ],
        ),
    ]
