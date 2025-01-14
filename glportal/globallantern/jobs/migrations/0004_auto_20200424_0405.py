# Generated by Django 3.0.5 on 2020-04-23 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0001_initial'),
        ('jobs', '0003_auto_20200424_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_post_skill_set',
            name='skill_set_id',
        ),
        migrations.AlterField(
            model_name='job_location',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job_post',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job_post_skill_set',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='seeker.skill_set', unique=True),
        ),
        migrations.AlterField(
            model_name='job_type',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
