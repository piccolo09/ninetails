# Generated by Django 3.2.7 on 2021-11-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0006_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otherschool',
            field=models.CharField(blank=True, help_text='Enter The School Name', max_length=255, null=True, verbose_name='Your School Name'),
        ),
    ]
