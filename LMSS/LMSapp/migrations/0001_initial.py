# Generated by Django 4.0.4 on 2022-04-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ABB',
            fields=[
                ('Book_id', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=500)),
                ('WriterName', models.CharField(max_length=500)),
                ('stname', models.CharField(max_length=500)),
                ('stemail', models.CharField(max_length=500)),
                ('stdept', models.CharField(max_length=500)),
                ('Dateretreived', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='IB',
            fields=[
                ('Book_id', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=500)),
                ('WriterName', models.CharField(max_length=500)),
                ('stname', models.CharField(max_length=500)),
                ('stemail', models.CharField(max_length=500)),
                ('stdept', models.CharField(max_length=500)),
                ('DateAdded', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NB',
            fields=[
                ('Book_id', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=500)),
                ('WriterName', models.CharField(max_length=500)),
                ('DateAdded', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RB',
            fields=[
                ('Book_id', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=500)),
                ('WriterName', models.CharField(max_length=500)),
                ('stname', models.CharField(max_length=500)),
                ('stemail', models.CharField(max_length=500)),
                ('stdept', models.CharField(max_length=500)),
                ('Datereturned', models.DateField()),
            ],
        ),
    ]
