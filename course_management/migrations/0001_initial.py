# Generated by Django 3.2.7 on 2021-11-14 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_management', '0008_remove_student_otherschool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter The Course Title', max_length=255, verbose_name='Course Name')),
                ('description', models.TextField(blank=True, help_text='Enter The Course Description', null=True, verbose_name='Course Description')),
                ('keywords', models.TextField(blank=True, help_text='eg: mathematics,BusinessStudies,Management', null=True, verbose_name='SEO keys')),
                ('monthly_rate', models.PositiveIntegerField(verbose_name='Monthly Rate')),
                ('yearly_rate', models.PositiveIntegerField(verbose_name='Yearly Rate')),
                ('promo_video_link', models.URLField(verbose_name='Promotion Link')),
                ('status', models.CharField(choices=[('P', 'PUBLISHED'), ('NP', 'NOT PUBLISHED')], default='NP', max_length=2)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='school_management.school', verbose_name='Cousre Owned By')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='school_management.teacher', verbose_name='Cousre Owned By')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Registered Courses',
            },
        ),
    ]
