# Generated by Django 5.0.3 on 2024-04-15 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('datadenascimento', models.DateField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
    ]
