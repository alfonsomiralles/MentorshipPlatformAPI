# Generated by Django 3.2.10 on 2023-04-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0002_auto_20230412_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non-binary'), ('O', 'Other')], max_length=1),
        ),
    ]
