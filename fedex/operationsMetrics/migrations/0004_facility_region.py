# Generated by Django 4.1.2 on 2022-11-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operationsMetrics', '0003_alter_packagesperhour_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='ISBN')),
                ('facility', models.ManyToManyField(help_text='Select a genre for this book', to='operationsMetrics.facility')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
