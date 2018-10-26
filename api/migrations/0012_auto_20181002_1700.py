# Generated by Django 2.1.1 on 2018-10-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181001_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agelimit',
            name='content',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='agelimit',
            name='text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='content',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='applicationfee',
            name='text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='content',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='importantdates',
            name='content',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='importantdates',
            name='text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancydetail',
            name='content',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancydetail',
            name='text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
