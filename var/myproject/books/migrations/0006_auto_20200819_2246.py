# Generated by Django 3.1 on 2020-08-19 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200817_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantity',
            old_name='Stock',
            new_name='stock',
        ),
    ]
