# Generated by Django 2.1 on 2019-03-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0020_merge_20190303_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='invoice_no',
            field=models.IntegerField(default=0),
        ),
    ]
