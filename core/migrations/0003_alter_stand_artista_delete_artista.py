# Generated by Django 5.0.6 on 2024-06-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_stand_artista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stand',
            name='artista',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Artista',
        ),
    ]
