# Generated by Django 4.0.5 on 2022-06-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest1', '0002_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
    ]
