# Generated by Django 2.0.7 on 2018-07-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uesrname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]