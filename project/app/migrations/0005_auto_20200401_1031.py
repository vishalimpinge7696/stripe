# Generated by Django 3.0.4 on 2020-04-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200331_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.FileField(default='SOME STRING', help_text='Upload only .png, .jpg & .jpeg image extension.', upload_to='images/'),
        ),
    ]