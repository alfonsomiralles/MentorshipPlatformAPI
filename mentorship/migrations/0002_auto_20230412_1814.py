# Generated by Django 3.2.10 on 2023-04-12 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentorship',
            old_name='mentor_id',
            new_name='mentor',
        ),
        migrations.RenameField(
            model_name='mentorship',
            old_name='project_id',
            new_name='project',
        ),
    ]