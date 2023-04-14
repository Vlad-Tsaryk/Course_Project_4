# Generated by Django 3.2.15 on 2023-03-21 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': "Одиниця виміру з таким ім'ям вже існує!"}, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Послуга з такою назвою вже існує!'}, max_length=50, unique=True)),
                ('is_counter', models.BooleanField(default=False)),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='admin_service.unit')),
            ],
        ),
    ]