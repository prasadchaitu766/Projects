# Generated by Django 2.1.7 on 2019-03-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcCitizen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen_register',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='citizen_register',
            name='username',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
