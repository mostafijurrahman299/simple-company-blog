# Generated by Django 2.1.7 on 2019-06-25 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190625_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_drafe',
            new_name='is_draft',
        ),
    ]