# Generated by Django 3.2.10 on 2023-04-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0003_alter_mentor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mentors',
            field=models.ManyToManyField(through='mentorship.Mentorship', to='mentorship.Mentor'),
        ),
    ]