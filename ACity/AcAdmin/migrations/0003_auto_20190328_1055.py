# Generated by Django 2.1.7 on 2019-03-28 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcAdmin', '0002_auto_20190327_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='name',
        ),
    ]
