# Generated by Django 4.1.2 on 2022-11-01 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operationsMetrics', '0002_exceptions_dex_exception'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packagesperhour',
            options={'ordering': ['-name']},
        ),
    ]
