# Generated by Django 3.2.6 on 2022-06-15 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_auto_20220615_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retweet',
            name='fechaRetweet',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 17, 38, 38, 667911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 17, 38, 38, 667500, tzinfo=utc)),
        ),
    ]
