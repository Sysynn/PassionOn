# Generated by Django 3.2.18 on 2023-05-11 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
        ('accounts', '0002_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('bought_on', models.DateTimeField(auto_now_add=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.cloth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.cloth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
