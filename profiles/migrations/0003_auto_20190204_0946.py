# Generated by Django 2.1.5 on 2019-02-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='description',
            field=models.TextField(default='Default Description text'),
        ),
    ]
