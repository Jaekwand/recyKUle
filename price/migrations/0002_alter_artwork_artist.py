# Generated by Django 3.2.9 on 2021-11-29 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.artist'),
        ),
    ]
