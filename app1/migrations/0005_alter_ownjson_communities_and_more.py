# Generated by Django 4.1.5 on 2023-05-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_formats_ownjson_rename_defaultexample_dataformats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownjson',
            name='communities',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='ownjson',
            name='convertation_formats',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='ownjson',
            name='data_formats',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
