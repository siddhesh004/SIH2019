# Generated by Django 2.1 on 2019-03-03 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0014_auto_20190303_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptdata',
            name='ip_address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='receiptdata',
            name='timestamp',
            field=models.CharField(default='', max_length=50),
        ),
    ]
