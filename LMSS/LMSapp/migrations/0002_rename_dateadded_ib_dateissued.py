# Generated by Django 4.0.4 on 2022-04-25 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ib',
            old_name='DateAdded',
            new_name='DateIssued',
        ),
    ]