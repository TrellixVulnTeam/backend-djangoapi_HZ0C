# Generated by Django 3.2.6 on 2021-08-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisco',
            name='ativo',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='fisco',
            name='dataAlteracao',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
