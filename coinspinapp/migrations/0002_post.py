# Generated by Django 4.2 on 2023-04-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinspinapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Detail', models.TextField()),
                ('Link', models.URLField()),
                ('Title', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
