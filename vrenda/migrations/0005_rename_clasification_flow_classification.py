# Generated by Django 5.0.1 on 2024-02-01 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vrenda', '0004_remove_entrada_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flow',
            old_name='clasification',
            new_name='classification',
        ),
    ]
