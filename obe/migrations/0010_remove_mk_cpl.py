# Generated by Django 4.2.15 on 2024-09-06 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obe', '0009_alter_subcpmk_cpl_cpmk_mk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mk',
            name='cpl',
        ),
    ]
