# Generated by Django 4.1.7 on 2023-04-26 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0002_questionchoice_topic_questionlongterm_topic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionchoice',
            name='category',
        ),
        migrations.RemoveField(
            model_name='questionlongterm',
            name='category',
        ),
        migrations.RemoveField(
            model_name='questionshortterm',
            name='category',
        ),
        migrations.AddField(
            model_name='questionchoice',
            name='somo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.masomo'),
        ),
        migrations.AddField(
            model_name='questionlongterm',
            name='somo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.masomo'),
        ),
        migrations.AddField(
            model_name='questionshortterm',
            name='somo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.masomo'),
        ),
    ]