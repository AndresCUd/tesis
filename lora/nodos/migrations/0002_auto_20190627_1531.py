# Generated by Django 2.2.2 on 2019-06-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lista',
            old_name='tamaño',
            new_name='tamano',
        ),
        migrations.RemoveField(
            model_name='lista',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='lista',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='datos/'),
        ),
    ]
