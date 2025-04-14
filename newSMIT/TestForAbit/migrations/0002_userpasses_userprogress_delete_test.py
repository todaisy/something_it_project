# Generated by Django 4.2.18 on 2025-04-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestForAbit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1_finish', models.BooleanField(default=False)),
                ('test1_start', models.BooleanField(default=False)),
                ('test2_finish', models.BooleanField(default=False)),
                ('test2_start', models.BooleanField(default=False)),
                ('test3_finish', models.BooleanField(default=False)),
                ('test3_start', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('test_id', models.IntegerField()),
                ('finish', models.BooleanField(default=False)),
                ('list_answers', models.JSONField(default=list)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
