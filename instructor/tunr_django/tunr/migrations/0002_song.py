# Generated by Django 5.0 on 2023-12-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('preview_url', models.TextField()),
            ],
        ),
    ]
