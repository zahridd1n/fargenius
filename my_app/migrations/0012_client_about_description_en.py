# Generated by Django 5.0.6 on 2024-06-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_about_image_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_about',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]
