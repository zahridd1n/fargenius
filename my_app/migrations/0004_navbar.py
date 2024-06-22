# Generated by Django 5.0.6 on 2024-06-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_porfolio_photo1_alter_porfolio_photo2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
                ('logo_dark', models.ImageField(upload_to='logo/photo', verbose_name='Dark mode uchun logo ')),
                ('logo_light', models.ImageField(upload_to='logo/photo', verbose_name='Dark mode uchun logo ')),
                ('phone', models.CharField(max_length=13)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
