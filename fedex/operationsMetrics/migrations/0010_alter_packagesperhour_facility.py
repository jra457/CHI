# Generated by Django 4.1.2 on 2022-11-03 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operationsMetrics', '0009_alter_packagesperhour_facility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagesperhour',
            name='facility',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='operationsMetrics.facility'),
        ),
    ]
