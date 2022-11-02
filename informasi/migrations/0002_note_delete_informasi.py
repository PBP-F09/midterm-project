# Generated by Django 4.1 on 2022-10-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokasi', models.CharField(blank=True, default='', max_length=32)),
                ('tanggal', models.DateField(default='')),
                ('waktu', models.CharField(default='', max_length=32)),
                ('kapasitas_balita', models.IntegerField(default='')),
                ('uploaded', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-uploaded',),
            },
        ),
        migrations.DeleteModel(
            name='Informasi',
        ),
    ]