# Generated by Django 3.2.18 on 2023-05-17 05:46

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_auto_20230515_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='size',
            field=models.CharField(choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('Free', 'free')], default='free', max_length=15),
        ),
        migrations.CreateModel(
            name='ClothDescriptionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='')),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.cloth')),
            ],
        ),
    ]
