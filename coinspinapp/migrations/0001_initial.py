# Generated by Django 4.2 on 2023-04-12 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coinmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('detial', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Coinmaster',
            },
        ),
    ]