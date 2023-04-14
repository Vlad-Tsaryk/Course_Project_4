# Generated by Django 3.2.15 on 2023-03-21 22:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='website/about_page')),
                ('additional_title', models.CharField(max_length=70)),
                ('additional_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TariffPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField()),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='admin_website.seo')),
            ],
        ),
        migrations.CreateModel(
            name='TariffBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='website/tariff_page/blocks')),
                ('title', models.CharField(max_length=70)),
                ('tariff_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_website.tariffpage')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='admin_website.seo')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='website/service_page/blocks')),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField()),
                ('service_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_website.servicepage')),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='website/main_page')),
                ('image2', models.ImageField(upload_to='website/main_page')),
                ('image3', models.ImageField(upload_to='website/main_page')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=70)),
                ('show_app_urls', models.BooleanField(default=True)),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='admin_website.seo')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='website/about_page/gallery')),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_website.aboutpage')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='website/about_page/documents')),
                ('title', models.CharField(max_length=70)),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_website.aboutpage')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField()),
                ('site_url', models.URLField()),
                ('full_name', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('map_code', models.TextField()),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='admin_website.seo')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='website/main_page/blocks')),
                ('main_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_website.mainpage')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='website/about_page/additional_gallery')),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_website.aboutpage')),
            ],
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='seo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='admin_website.seo'),
        ),
    ]
