# Generated by Django 4.1.2 on 2022-12-04 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opMetrics', '0002_employee_alter_location_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='district',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='division',
            old_name='division',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='region',
            new_name='name',
        ),
    ]
