# Generated by Django 4.0.4 on 2022-04-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0002_rename_dateadded_ib_dateissued'),
    ]

    operations = [
        migrations.CreateModel(
            name='NAB',
            fields=[
                ('Book_id', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=500)),
                ('WriterName', models.CharField(max_length=500)),
                ('DateAdded', models.DateField()),
            ],
        ),
    ]
