# Generated by Django 3.0.dev20190627131022 on 2019-06-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=200)),
                ('tamaño', models.IntegerField(default=0)),
            ],
        ),
    ]