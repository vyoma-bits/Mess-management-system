# Generated by Django 4.2.7 on 2023-11-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.CharField(default=True, max_length=350),
            preserve_default=False,
        ),
    ]
