# Generated by Django 3.0.5 on 2020-04-20 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('seeker', '0001_initial'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AlterField(
            model_name='job_post_skill_set',
            name='job_post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job_post'),
        ),
        migrations.AlterField(
            model_name='job_post_skill_set',
            name='skill_set_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seeker.skill_set'),
        ),
    ]
