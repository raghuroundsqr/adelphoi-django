# Generated by Django 2.2.7 on 2019-12-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0011_auto_20191212_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltests',
            name='FAST_CaregiverAdvocacyScore',
            field=models.FloatField(db_column='FAST_CaregiverAdvocacyScore'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='FAST_FamilyTogetherScore',
            field=models.FloatField(db_column='FAST_FamilyTogetherScore'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='Screening_tool_Trauma',
            field=models.FloatField(db_column='Screening_tool_Trauma'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='abuse_neglect',
            field=models.FloatField(choices=[(0, 'no'), (1, 'yes')], db_column='abuse_neglect'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_CareGiverStrengths',
            field=models.FloatField(db_column='CANS_CareGiverStrengths'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_Culture',
            field=models.FloatField(db_column='CANS_Culture'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_LifeFunctioning',
            field=models.FloatField(db_column='CANS_LifeFunctioning'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_Trauma_Exp',
            field=models.FloatField(db_column='CANS_Trauma_Exp'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_YouthBehavior',
            field=models.FloatField(db_column='CANS_YouthBehavior'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_YouthRisk',
            field=models.FloatField(db_column='CANS_YouthRisk'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='cans_YouthStrengths',
            field=models.FloatField(db_column='CANS_YouthStrengths'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='client_self_harm',
            field=models.FloatField(db_column='Client_self_harm'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='fire_setting',
            field=models.FloatField(db_column='fire_setting', null=True),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='level_of_aggression',
            field=models.FloatField(db_column='level_of_aggression', null=True),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_Attitude_Score',
            field=models.FloatField(blank=True, db_column='YLS_Attitude_Score'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_Edu_Employ_Score',
            field=models.FloatField(blank=True, db_column='YLS_Edu_Employ_Score'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_FamCircumstances_Score',
            field=models.FloatField(blank=True, db_column='YLS_FamCircumstances_Score'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_Leisure_Score',
            field=models.FloatField(blank=True, db_column='YLS_Leisure_Score'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_Peer_Score',
            field=models.FloatField(blank=True, db_column='YLS_Peer_Score'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_Personality_Score',
            field=models.FloatField(blank=True, db_column='YLS_Personality_Score'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_PriorCurrentOffenses_Score',
            field=models.FloatField(blank=True, db_column='YLS_PriorCurrentOffenses_Score'),
        ),
        migrations.AlterField(
            model_name='modeltests',
            name='yls_Subab_Score',
            field=models.FloatField(blank=True, db_column='YLS_Subab_Score'),
        ),
    ]
