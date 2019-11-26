# Generated by Django 2.2.7 on 2019-11-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_code', models.IntegerField(db_column='Client_code')),
                ('Gender', models.IntegerField(db_column='Gender')),
                ('PrimaryRacecode', models.IntegerField(db_column='PrimaryRacecode')),
                ('LS_Type', models.IntegerField(db_column='LS_Type')),
                ('AgeAtEpisodeStart', models.IntegerField(db_column='AgeAtEpisodeStart')),
                ('EpisodeNumber', models.IntegerField(db_column='EpisodeNumber')),
                ('CYF_code', models.IntegerField(db_column='CYF_code')),
                ('AgeAtEnrollStart', models.IntegerField(db_column='AgeAtEnrollStart')),
                ('RefSourceCode', models.IntegerField(db_column='RefSourceCode')),
                ('Termination_directly_to_AV', models.IntegerField(db_column='Termination_directly_to_AV')),
                ('Client_self_harm', models.IntegerField(db_column='Client_self_harm')),
                ('YLS_PriorCurrentOffenses_Score', models.IntegerField(db_column='YLS_PriorCurrentOffenses_Score')),
                ('YLS_FamCircumstances_Score', models.IntegerField(db_column='YLS_FamCircumstances_Score')),
                ('YLS_Edu_Employ_Score', models.IntegerField(db_column='YLS_Edu_Employ_Score')),
                ('YLS_Peer_Score', models.IntegerField(db_column='YLS_Peer_Score')),
                ('YLS_Subab_Score', models.IntegerField(db_column='YLS_Subab_Score')),
                ('YLS_Leisure_Score', models.IntegerField(db_column='YLS_Leisure_Score')),
                ('YLS_Personality_Score', models.IntegerField(db_column='YLS_Personality_Score')),
                ('YLS_Attitude_Score', models.IntegerField(db_column='YLS_Attitude_Score')),
                ('Incarcerated_caregivers', models.IntegerField(db_column='Incarcerated_caregivers')),
                ('Incarcerated_siblings', models.IntegerField(db_column='Incarcerated_siblings')),
                ('Number_of_prior_AWOLS', models.IntegerField(db_column='Number_of_prior_AWOLS')),
                ('Animal_cruelty', models.IntegerField(db_column='Animal_cruelty')),
                ('sexually_acting_out_in_past_program', models.IntegerField(db_column='sexually_acting_out_in_past_program')),
                ('prior_hospitalizations', models.IntegerField(db_column='prior_hospitalizations')),
                ('Autism_Diagnosis', models.IntegerField(db_column='Autism_Diagnosis')),
                ('Borderline_Personality', models.IntegerField(db_column='Borderline_Personality')),
                ('Compliant_with_meds', models.IntegerField(db_column='Compliant_with_meds')),
                ('Death_Silblings', models.IntegerField(db_column='Death Silblings')),
                ('Death_Caregiver', models.IntegerField(db_column='Death_Caregiver')),
                ('Alcohol_Use', models.IntegerField(db_column='Alcohol_Use')),
                ('Drug_Use', models.IntegerField(db_column='Drug_Use')),
                ('Borderline_IQ', models.IntegerField(db_column='Borderline_IQ')),
                ('Significant_mental_health_symptoms', models.IntegerField(db_column='Significant_mental_health_symptoms')),
                ('Severe_mental_health_symptoms', models.IntegerField(db_column='Severe_mental_health_symptoms')),
                ('Number_of_prior_placements', models.IntegerField(db_column='Number_of_prior_placements')),
                ('Psychosis', models.IntegerField(db_column='Psychosis')),
                ('Reactive_Attachment_Disorder', models.IntegerField(db_column='Reactive_Attachment_Disorder')),
                ('Schizophrenia', models.IntegerField(db_column='Schizophrenia')),
                ('Number_of_foster_care_placements', models.IntegerField(db_column='Number_of_foster_care_placements')),
                ('Number_of_prior_treatment_terminations', models.IntegerField(db_column='Number_of_prior_treatment_terminations')),
                ('Length_of_time_since_living_at_home', models.IntegerField(db_column='Length_of_time_since_living_at_home')),
                ('CANS_LifeFunctioning', models.IntegerField(db_column='CANS_LifeFunctioning')),
                ('CANS_YouthStrengths', models.IntegerField(db_column='CANS_YouthStrengths')),
                ('CANS_CareGiverStrengths', models.IntegerField(db_column='CANS_CareGiverStrengths')),
                ('CANS_Culture', models.IntegerField(db_column='CANS_Culture')),
                ('CANS_YouthBehavior', models.IntegerField(db_column='CANS_YouthBehavior')),
                ('CANS_YouthRisk', models.IntegerField(db_column='CANS_YouthRisk')),
                ('CANS_Trauma_Exp', models.IntegerField(db_column='CANS_Trauma_Exp')),
            ],
        ),
        migrations.CreateModel(
            name='ModelTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_code', models.IntegerField(db_column='Client_code')),
                ('gender', models.IntegerField(choices=[(2, 'Male'), (1, 'Female')], db_column='Gender')),
                ('primaryRaceCode', models.IntegerField(choices=[(1, 'caucasian'), (2, 'African American'), (3, 'Hispanic'), (4, 'Others')], db_column='PrimaryRacecode')),
                ('ls_type', models.IntegerField(choices=[(1, 'voluntary'), (2, 'Dependent'), (3, 'Voluntary Delinquent'), (4, 'Dependent Delinquent'), (5, 'Delinquent')], db_column='LS_Type')),
                ('ageAtEpisodeStart', models.IntegerField(db_column='AgeAtEpisodeStart')),
                ('episode_number', models.IntegerField(db_column='EpisodeNumber')),
                ('CYF_code', models.IntegerField(choices=[(1, 'CYF'), (2, 'Juvenile Justice'), (3, 'MH')], db_column='CYF_code')),
                ('ageAtEnrollStart', models.IntegerField(db_column='AgeAtEnrollStart')),
                ('RefSourceCode', models.IntegerField(choices=[(1, 'Adams'), (2, 'Allegheny'), (3, 'Beaver'), (4, 'Bedford'), (5, 'Berks'), (6, 'Blair'), (7, 'Bucks'), (8, 'Butler'), (9, 'Cambria'), (10, 'Centre'), (11, 'Chester'), (12, 'Cumberland'), (13, 'Dauphin'), (14, 'Delaware'), (15, 'Erie'), (16, 'Fayette'), (17, 'Franklin'), (18, 'Huntingdon'), (19, 'Juniata'), (20, 'Kent'), (21, 'Lackawanna'), (22, 'Lancaster'), (23, 'Lebanon'), (24, 'Lehigh'), (25, 'Lycoming'), (26, 'Monroe'), (27, 'Montgomery'), (28, 'Montour'), (29, 'Northumberland'), (30, 'Perry'), (31, 'Philadelphia'), (32, 'Pike'), (34, 'Snyder'), (35, 'Tioga'), (36, 'Washington'), (37, 'Westmoreland'), (38, 'York'), (39, 'Armstrong'), (40, 'Columbia'), (41, 'Crawford'), (42, 'Cayahoga OH'), (43, 'Franklin OH'), (44, 'Greene'), (45, 'Indiana'), (46, 'Lawrence'), (47, 'MH'), (48, 'Mckean'), (49, 'Mercer'), (50, 'outside tri-county'), (51, 'Northampton'), (52, 'Pike'), (53, 'Schukill'), (54, 'Somerset'), (55, 'Union'), (56, 'Venango')], db_column='RefSourceCode')),
                ('termination_directly_to_AV', models.IntegerField(choices=[(0, 'no'), (1, 'unknown'), (2, 'one'), (3, 'two or more')], db_column='Termination_directly_to_AV')),
                ('client_self_harm', models.IntegerField(db_column='Client_self_harm')),
                ('yls_PriorCurrentOffenses_Score', models.IntegerField(db_column='YLS_PriorCurrentOffenses_Score')),
                ('yls_FamCircumstances_Score', models.IntegerField(db_column='YLS_FamCircumstances_Score')),
                ('yls_Edu_Employ_Score', models.IntegerField(db_column='YLS_Edu_Employ_Score')),
                ('yls_Peer_Score', models.IntegerField(db_column='YLS_Peer_Score')),
                ('yls_Subab_Score', models.IntegerField(db_column='YLS_Subab_Score')),
                ('yls_Leisure_Score', models.IntegerField(db_column='YLS_Leisure_Score')),
                ('yls_Personality_Score', models.IntegerField(db_column='YLS_Personality_Score')),
                ('yls_Attitude_Score', models.IntegerField(db_column='YLS_Attitude_Score')),
                ('cans_LifeFunctioning', models.IntegerField(db_column='CANS_LifeFunctioning')),
                ('cans_YouthStrengths', models.IntegerField(db_column='CANS_YouthStrengths')),
                ('cans_CareGiverStrengths', models.IntegerField(db_column='CANS_CareGiverStrengths')),
                ('cans_Culture', models.IntegerField(db_column='CANS_Culture')),
                ('cans_YouthBehavior', models.IntegerField(db_column='CANS_YouthBehavior')),
                ('cans_YouthRisk', models.IntegerField(db_column='CANS_YouthRisk')),
                ('cans_Trauma_Exp', models.IntegerField(db_column='CANS_Trauma_Exp')),
                ('incarcerated_caregivers', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Incarcerated_caregivers')),
                ('incarcerated_siblings', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Incarcerated_siblings')),
                ('number_of_prior_AWOLS', models.IntegerField(choices=[(0, 'none'), (1, 'one'), (2, 'two'), (3, 'many')], db_column='Number_of_prior_AWOLS')),
                ('animal_cruelty', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Animal_cruelty')),
                ('sexually_acting_out_in_past_program', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='sexually_acting_out_in_past_program')),
                ('prior_hospitalizations', models.IntegerField(db_column='prior_hospitalizations')),
                ('autism_Diagnosis', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Autism_Diagnosis')),
                ('borderline_Personality', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Borderline_Personality')),
                ('compliant_with_meds', models.IntegerField(choices=[(0, 'no'), (1, 'yes'), (9, 'N / A')], db_column='Compliant_with_meds')),
                ('severe_mental_health_symptoms', models.IntegerField(db_column='Severe_mental_health_symptoms')),
                ('number_of_prior_treatment_terminations', models.IntegerField(db_column='Number_of_prior_treatment_terminations')),
                ('length_of_time_since_living_at_home', models.IntegerField(db_column='Length_of_time_since_living_at_home')),
                ('death_Silblings', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Death Silblings')),
                ('death_Caregiver', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Death_Caregiver')),
                ('alcohol_Use', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Alcohol_Use')),
                ('drug_Use', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Drug_Use')),
                ('borderline_IQ', models.IntegerField(choices=[(0, '70+, or not listed assumed 70+'), (1, '<70')], db_column='Borderline_IQ')),
                ('significant_mental_health_symptoms', models.IntegerField(choices=[(0, 'no ER/hospitalizations'), (1, 'last 3 months'), (2, '6 months ago'), (3, '9 months ago'), (4, '1 year or more ago')], db_column='Significant_mental_health_symptoms')),
                ('number_of_prior_placements', models.IntegerField(choices=[(0, 'no'), (1, 'one'), (2, 'two'), (3, 'three or more')], db_column='Number_of_prior_placements')),
                ('psychosis', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Psychosis')),
                ('reactive_Attachment_Disorder', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Reactive_Attachment_Disorder')),
                ('schizophrenia', models.IntegerField(choices=[(0, 'no'), (1, 'yes')], db_column='Schizophrenia')),
                ('number_of_foster_care_placements', models.IntegerField(choices=[(0, 'no'), (1, 'one'), (2, 'two'), (3, 'three or more')], db_column='Number_of_foster_care_placements')),
                ('hist_of_prior_program_SAO', models.IntegerField(db_column='Hist_of_prior_program_SAO', default=999)),
                ('program', models.IntegerField(db_column='Program')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='TestMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_code', models.IntegerField(blank=True, db_column='Client_code', null=True)),
                ('prior_hospitalizations', models.IntegerField(blank=True, db_column='prior_hospitalizations', null=True)),
            ],
            options={
                'db_table': 'TestMod',
            },
        ),
        migrations.CreateModel(
            name='TestModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_code', models.IntegerField(blank=True, db_column='Client_code', null=True)),
                ('First_name', models.CharField(blank=True, db_column='First_name', max_length=100, null=True)),
                ('Last_name', models.CharField(blank=True, db_column='Last_name', max_length=100, null=True)),
                ('Gender', models.IntegerField(blank=True, choices=[(2, 'Male'), (1, 'Female')], db_column='Gender', null=True)),
                ('PrimaryRacecode', models.IntegerField(blank=True, choices=[(1, 'caucasian'), (2, 'African American'), (3, 'Hispanic'), (4, 'Others')], db_column='PrimaryRacecode', null=True)),
                ('LS_Type', models.IntegerField(blank=True, choices=[(1, 'voluntary'), (2, 'Dependent'), (3, 'Voluntary Delinquent'), (4, 'Dependent Delinquent'), (5, 'Delinquent')], db_column='LS_Type', null=True)),
                ('AgeAtEpisodeStart', models.IntegerField(blank=True, db_column='AgeAtEpisodeStart', null=True)),
                ('EpisodeNumber', models.IntegerField(blank=True, db_column='EpisodeNumber', null=True)),
                ('CYF_code', models.IntegerField(blank=True, choices=[(1, 'CYF'), (2, 'Juvenile Justice'), (3, 'MH')], db_column='CYF_code', null=True)),
                ('AgeAtEnrollStart', models.IntegerField(blank=True, db_column='AgeAtEnrollStart', null=True)),
                ('RefSourceCode', models.IntegerField(blank=True, choices=[(1, 'Adams'), (2, 'Allegheny'), (3, 'Beaver'), (4, 'Bedford'), (5, 'Berks'), (6, 'Blair'), (7, 'Bucks'), (8, 'Butler'), (9, 'Cambria'), (10, 'Centre'), (11, 'Chester'), (12, 'Cumberland'), (13, 'Dauphin'), (14, 'Delaware'), (15, 'Erie'), (16, 'Fayette'), (17, 'Franklin'), (18, 'Huntingdon'), (19, 'Juniata'), (20, 'Kent'), (21, 'Lackawanna'), (22, 'Lancaster'), (23, 'Lebanon'), (24, 'Lehigh'), (25, 'Lycoming'), (26, 'Monroe'), (27, 'Montgomery'), (28, 'Montour'), (29, 'Northumberland'), (30, 'Perry'), (31, 'Philadelphia'), (32, 'Pike'), (34, 'Snyder'), (35, 'Tioga'), (36, 'Washington'), (37, 'Westmoreland'), (38, 'York'), (39, 'Armstrong'), (40, 'Columbia'), (41, 'Crawford'), (42, 'Cayahoga OH'), (43, 'Franklin OH'), (44, 'Greene'), (45, 'Indiana'), (46, 'Lawrence'), (47, 'MH'), (48, 'Mckean'), (49, 'Mercer'), (50, 'outside tri-county'), (51, 'Northampton'), (52, 'Pike'), (53, 'Schukill'), (54, 'Somerset'), (55, 'Union'), (56, 'Venango')], db_column='RefSourceCode', null=True)),
                ('Incarcerated_caregivers', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], db_column='Incarcerated_caregivers', null=True)),
                ('Incarcerated_siblings', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], db_column='Incarcerated_siblings', null=True)),
                ('Number_of_prior_AWOLS', models.IntegerField(blank=True, choices=[(0, 'none'), (1, 'one'), (2, 'two'), (3, 'many')], db_column='Number_of_prior_AWOLS', null=True)),
                ('Animal_cruelty', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], db_column='Animal_cruelty', null=True)),
                ('sexually_acting_out_in_past_program', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], db_column='sexually_acting_out_in_past_program', null=True)),
                ('prior_hospitalizations', models.IntegerField(blank=True, db_column='prior_hospitalizations', null=True)),
                ('Termination_directly_to_AV', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'unknown'), (2, 'one'), (3, 'two or more')], db_column='Termination_directly_to_AV', null=True)),
                ('Autism_Diagnosis', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], db_column='Autism_Diagnosis', null=True)),
                ('Borderline_Personality', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], db_column='Borderline_Personality', null=True)),
                ('Compliant_with_meds', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes'), (9, 'N / A')], db_column='Compliant_with_meds', null=True)),
            ],
        ),
    ]
