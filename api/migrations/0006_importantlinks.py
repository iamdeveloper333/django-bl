# Generated by Django 2.1.1 on 2018-10-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_agelimit_vacancydetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply', models.CharField(max_length=200)),
                ('notification', models.CharField(max_length=200)),
                ('syllabus', models.CharField(max_length=200)),
                ('o_website', models.CharField(max_length=200)),
                ('extra_info', models.CharField(max_length=200)),
            ],
        ),
    ]