# Generated by Django 4.0.3 on 2022-07-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.CharField(editable=False, max_length=13, primary_key=True, serialize=False, unique=True),
        ),
    ]
