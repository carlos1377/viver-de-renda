# Generated by Django 5.0.1 on 2024-01-31 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vrenda', '0003_alter_entrada_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='email',
        ),
    ]