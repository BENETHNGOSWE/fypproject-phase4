# Generated by Django 4.1.7 on 2023-04-11 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FYPAPP', '0001_initial'),
        ('mtihani', '0009_mtihani_delete_examquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtihani',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FYPAPP.masomo'),
        ),
    ]