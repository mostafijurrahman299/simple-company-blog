# Generated by Django 2.1.7 on 2019-06-24 21:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190625_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]