# Generated by Django 3.2.18 on 2023-05-12 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230511_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaselog',
            old_name='bought_on',
            new_name='bought_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='carts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='purchase_logs',
        ),
    ]
