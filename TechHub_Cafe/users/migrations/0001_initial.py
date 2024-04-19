# Generated by Django 5.0.4 on 2024-04-19 11:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('computer_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_specifications', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('id_proof', models.CharField(choices=[('aadhar', 'AADHAR'), ('pan', 'PAN'), ('voter', 'VOTER')], default='AADHAR', max_length=20)),
                ('id_number', models.CharField(max_length=20)),
                ('user', models.OneToOneField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], default='USER', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('computer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.computer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
