# Generated by Django 2.2.7 on 2019-11-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0004_auto_20191125_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeltests',
            name='sexually_acting_out_in_past_program',
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='hist_of_prior_program_SAO',
            field=models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Hist_of_prior_program_SAO'),
        ),
    ]
