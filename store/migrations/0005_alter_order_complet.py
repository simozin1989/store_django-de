# Generated by Django 3.2.9 on 2021-11-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20211115_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complet',
            field=models.BooleanField(default=False),
        ),
    ]
