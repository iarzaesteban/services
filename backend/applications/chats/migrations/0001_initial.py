# Generated by Django 4.2.9 on 2024-10-07 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('multimedia', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(choices=[('texto', 'Texto'), ('imagen', 'Imagen'), ('video', 'Video')], max_length=20)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
