# Generated by Django 4.2.18 on 2025-04-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avalible', models.BooleanField(default=False)),
                ('descript', models.TextField(default='')),
            ],
        ),
    ]
