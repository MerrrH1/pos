# Generated by Django 5.1.2 on 2024-11-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_app', '0006_alter_menuresto_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuresto',
            name='description',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
    ]
