# Generated by Django 2.0 on 2019-03-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0013_merge_20190302_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='receiptdata',
            name='original_filename',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
