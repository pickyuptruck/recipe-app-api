# Generated by Django 2.1.15 on 2020-03-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
