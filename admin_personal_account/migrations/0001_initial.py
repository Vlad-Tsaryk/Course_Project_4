# Generated by Django 3.2.15 on 2023-03-21 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_apartment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Активний', 'Активний'), ('Вимкнено', 'Вимкнено')], max_length=9)),
                ('number', models.CharField(max_length=50, unique=True)),
                ('apartment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_apartment.apartment')),
            ],
        ),
    ]
