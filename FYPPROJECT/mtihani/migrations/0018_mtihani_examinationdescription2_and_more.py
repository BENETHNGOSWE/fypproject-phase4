# Generated by Django 4.1.7 on 2023-04-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtihani', '0017_mtihani_examinationdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtihani',
            name='examinationDescription2',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='mtihani',
            name='examinationDescription3',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mtihani',
            name='examinationDescription',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
