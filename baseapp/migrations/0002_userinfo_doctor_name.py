# Generated by Django 5.0 on 2024-02-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='doctor_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
