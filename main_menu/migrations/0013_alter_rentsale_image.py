# Generated by Django 4.1.2 on 2022-11-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0012_alter_rentsale_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentsale',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]