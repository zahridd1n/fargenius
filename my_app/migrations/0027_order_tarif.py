# Generated by Django 5.0.6 on 2024-11-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0026_alter_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tarif',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]
