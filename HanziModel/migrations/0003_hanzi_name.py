# Generated by Django 2.1.7 on 2019-02-20 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HanziModel', '0002_remove_hanzi_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hanzi',
            name='name',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]