# Generated by Django 2.0.7 on 2018-07-24 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_register_con_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='uesrname',
            new_name='username',
        ),
    ]