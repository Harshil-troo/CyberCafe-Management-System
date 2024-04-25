# Generated by Django 5.0.4 on 2024-04-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('computer_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_name', models.CharField(max_length=255)),
                ('processor', models.CharField(max_length=255)),
                ('ram', models.IntegerField()),
                ('operating_system', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
