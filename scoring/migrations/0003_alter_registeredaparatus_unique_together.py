# Generated by Django 3.2.6 on 2021-08-09 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0002_competitioninformation'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registeredaparatus',
            unique_together={('aparatus_name', 'gymnast')},
        ),
    ]
