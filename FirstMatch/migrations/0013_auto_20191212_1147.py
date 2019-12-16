# Generated by Django 2.2.7 on 2019-12-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0012_auto_20191212_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltests',
            name='FAST_CaregiverAdvocacyScore',
            field=models.FloatField(blank=True, db_column='FAST_CaregiverAdvocacyScore'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='FAST_FamilyTogetherScore',
            field=models.FloatField(blank=True, db_column='FAST_FamilyTogetherScore'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='Screening_tool_Trauma',
            field=models.FloatField(blank=True, db_column='Screening_tool_Trauma'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_CareGiverStrengths',
            field=models.FloatField(blank=True, db_column='CANS_CareGiverStrengths'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_Culture',
            field=models.FloatField(blank=True, db_column='CANS_Culture'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_LifeFunctioning',
            field=models.FloatField(blank=True, db_column='CANS_LifeFunctioning'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_Trauma_Exp',
            field=models.FloatField(blank=True, db_column='CANS_Trauma_Exp'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_YouthBehavior',
            field=models.FloatField(blank=True, db_column='CANS_YouthBehavior'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_YouthRisk',
            field=models.FloatField(blank=True, db_column='CANS_YouthRisk'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_YouthStrengths',
            field=models.FloatField(blank=True, db_column='CANS_YouthStrengths'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='client_self_harm',
            field=models.FloatField(blank=True, db_column='Client_self_harm'),
        ),
    ]
