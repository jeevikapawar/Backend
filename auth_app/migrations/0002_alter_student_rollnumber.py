# Generated by Django 5.0.4 on 2024-04-10 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='RollNumber',
            field=models.BigIntegerField(default=0),
        ),
    ]