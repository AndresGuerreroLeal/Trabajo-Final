# Generated by Django 3.2.4 on 2021-07-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nuevo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='productos/photos')),
                ('descri', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
