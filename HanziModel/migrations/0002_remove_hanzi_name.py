# Generated by Django 2.1.7 on 2019-02-20 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HanziModel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hanzi',
            name='name',
        ),
    ]
