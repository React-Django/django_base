# Generated by Django 3.0.7 on 2020-07-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='updated_by',
            field=models.CharField(default='', max_length=255),
        ),
    ]
