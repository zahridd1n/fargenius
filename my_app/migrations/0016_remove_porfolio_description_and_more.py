# Generated by Django 5.0.6 on 2024-06-23 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0015_remove_porfolio_about_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porfolio',
            name='description',
        ),
        migrations.RemoveField(
            model_name='porfolio',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='porfolio',
            name='description_ru',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
                ('subcat_title', models.TextField(blank=True, null=True)),
                ('subcat_title_ru', models.TextField(blank=True, null=True)),
                ('subcat_title_en', models.TextField(blank=True, null=True)),
                ('sub_description', models.TextField(blank=True, null=True)),
                ('sub_description_ru', models.TextField(blank=True, null=True)),
                ('sub_description_en', models.TextField(blank=True, null=True)),
                ('sub_description1', models.TextField(blank=True, null=True)),
                ('sub_description1_ru', models.TextField(blank=True, null=True)),
                ('sub_description1_en', models.TextField(blank=True, null=True)),
                ('sub_photo', models.ImageField(upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting')),
                ('sub_photo1', models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting')),
                ('sub_photo2', models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting')),
                ('sub_photo3', models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting')),
                ('sub_photo4', models.ImageField(blank=True, null=True, upload_to='Service/photo', verbose_name='Portfolio rasmini kiriting')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='my_app.category', verbose_name='Qaysi categoriyaga oidligini kiriting')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
