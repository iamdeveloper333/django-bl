# Generated by Django 2.1.1 on 2018-09-19 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_importantdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('content', models.IntegerField(default=170)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Post')),
            ],
        ),
    ]
