# Generated by Django 2.1.7 on 2019-03-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=40)),
                ('password', models.IntegerField(max_length=10)),
                ('create_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
