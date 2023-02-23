# Generated by Django 4.0.6 on 2022-07-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='sobrenome')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
            ],
        ),
    ]