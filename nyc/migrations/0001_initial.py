# Generated by Django 4.1.5 on 2023-01-26 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='MutualAid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('category', models.CharField(max_length=254, verbose_name='Category')),
                ('website', models.URLField(max_length=254, verbose_name='Website')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('borough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyc.borough')),
            ],
        ),
    ]
