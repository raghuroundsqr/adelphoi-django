from djongo import models
from datetime import datetime
from django.urls import reverse
# from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import ArrayField
# Create your models here.

from jsonfield import JSONField

class TestModels(models.Model):

    GENDER_CHOICES = (
        (2, "Male"),
        (1, 'Female')
    )
    RACE_CHOICES = ((1,'caucasian'),
                    (2,'African American'),
                    (3,'Hispanic'),
                    (4,'Others'))
    LS_CHOICES = ((1,'voluntary'),
                  (2,'Dependent'),
                  (3,'Voluntary Delinquent'),
                  (4,'Dependent Delinquent'),
                  (5,'Delinquent'))
    REF_CHOICES = (
    (1,'Adams'), (2,'Allegheny'), (3,'Beaver'), (4,'Bedford'), (5,'Berks'),
    (6,'Blair'), (7,'Bucks'), (8,'Butler'), (9,'Cambria'), (10,'Centre'),(11,'Chester'),(12,'Cumberland'),
    (13,'Dauphin'), (14,'Delaware'), (15,'Erie'),(16,'Fayette'), (17,'Franklin'),(18,'Huntingdon'), (19,'Juniata'),
    (20,'Kent'),(21,'Lackawanna'), (22,'Lancaster'), (23,'Lebanon'), (24,'Lehigh'), (25,'Lycoming'),
    (26,'Monroe'), (27,'Montgomery'), (28,'Montour'), (29,'Northumberland'), (30,'Perry'),(31,'Philadelphia'),
    (32,'Pike'), (34,'Snyder'),(35,'Tioga'),(36,'Washington'), (37,'Westmoreland'), (38,'York'), (39,'Armstrong'),
    (40,'Columbia'), (41,'Crawford'), (42,'Cayahoga OH'), (43,'Franklin OH'), (44,'Greene'),(45,'Indiana'),(46,'Lawrence'),
    (47,'MH'), (48,'Mckean'),(49,'Mercer'),(50,'outside tri-county'),(51,'Northampton'), (52,'Pike'),(53,'Schukill'),
    (54,'Somerset'), (55,'Union'), (56,'Venango'))

    CYF_CHOICES = ((1,'CYF'),(2,'Juvenile Justice'), (3 ,'MH'))
    caregivers = ((0 ,'no'),(1,'yes'))
    siblings = ((0 ,'no'),(1,'yes'))
    awols = ((0,'none'),(1,'one'),(2,'two'),(3,'many'))
    cruelty = ((0 ,'no'),(1,'yes'))
    past_program = ((0 ,'no'),(1,'yes'))
    Termination_av = ((0,'no'),(1,'unknown'),(2,'one'),(3,'two or more'))
    Autism = ((0 ,'no'),(1,'yes'))
    border = ((0 ,'no'),(1,'yes'))
    complaint = ((0,'no'),(1,'yes'),(9,'N / A'))


    Client_code = models.IntegerField(db_column = 'Client_code', blank=True, null=True)
    First_name = models.CharField(db_column='First_name',max_length=100,blank=True, null=True)
    Last_name = models.CharField(db_column='Last_name', max_length=100, blank=True, null=True)
    Gender  = models.IntegerField(db_column = 'Gender',choices=GENDER_CHOICES, blank=True, null=True)
    PrimaryRacecode = models.IntegerField(db_column='PrimaryRacecode',choices = RACE_CHOICES, blank=True, null=True)
    LS_Type = models.IntegerField(db_column='LS_Type', choices = LS_CHOICES, blank=True, null=True)
    AgeAtEpisodeStart = models.IntegerField(db_column='AgeAtEpisodeStart', blank=True, null=True)
    EpisodeNumber = models.IntegerField(db_column='EpisodeNumber', blank=True, null=True)
    CYF_code = models.IntegerField(db_column='CYF_code',choices = CYF_CHOICES, blank=True, null=True)
    AgeAtEnrollStart = models.IntegerField(db_column='AgeAtEnrollStart', blank=True, null=True)
    RefSourceCode = models.IntegerField(db_column='RefSourceCode', choices = REF_CHOICES, blank=True, null=True)
    Incarcerated_caregivers = models.IntegerField(db_column='Incarcerated_caregivers',choices = caregivers, blank=True, null=True)
    Incarcerated_siblings = models.IntegerField(db_column='Incarcerated_siblings',choices = siblings,  blank=True, null=True)
    Number_of_prior_AWOLS = models.IntegerField(db_column='Number_of_prior_AWOLS',choices = awols, blank=True, null=True)
    Animal_cruelty = models.IntegerField(db_column='Animal_cruelty',choices = cruelty, blank=True, null=True)
    sexually_acting_out_in_past_program = models.IntegerField(db_column='sexually_acting_out_in_past_program',choices = past_program, blank=True, null=True)
    prior_hospitalizations = models.IntegerField(db_column='prior_hospitalizations', blank=True, null=True)
    Termination_directly_to_AV = models.IntegerField(db_column='Termination_directly_to_AV',choices = Termination_av,blank=True, null=True)
    Autism_Diagnosis = models.IntegerField(db_column='Autism_Diagnosis',choices = Autism,  blank=True, null=True)
    Borderline_Personality = models.IntegerField(db_column='Borderline_Personality', choices = border, blank=True, null=True)
    Compliant_with_meds = models.IntegerField(db_column='Compliant_with_meds', choices = complaint,blank=True, null=True)





     # = models.IntegerField(db_column = 'Age')
    # class Meta:
    #     managed = True
    #     db_table = 'TestModels_info'


class ModelTest(models.Model):
    Client_code = models.IntegerField(db_column = 'Client_code')
    Gender  = models.IntegerField(db_column = 'Gender')
    PrimaryRacecode = models.IntegerField(db_column='PrimaryRacecode')
    LS_Type = models.IntegerField(db_column='LS_Type')
    AgeAtEpisodeStart = models.IntegerField(db_column='AgeAtEpisodeStart')
    EpisodeNumber = models.IntegerField(db_column='EpisodeNumber')
    CYF_code = models.IntegerField(db_column='CYF_code')
    AgeAtEnrollStart = models.IntegerField(db_column='AgeAtEnrollStart')
    RefSourceCode = models.IntegerField(db_column='RefSourceCode')
    Termination_directly_to_AV = models.IntegerField(db_column='Termination_directly_to_AV')
    Client_self_harm = models.IntegerField(db_column='Client_self_harm')
    YLS_PriorCurrentOffenses_Score = models.IntegerField(db_column='YLS_PriorCurrentOffenses_Score')
    YLS_FamCircumstances_Score = models.IntegerField(db_column='YLS_FamCircumstances_Score')
    YLS_Edu_Employ_Score = models.IntegerField(db_column='YLS_Edu_Employ_Score')
    YLS_Peer_Score = models.IntegerField(db_column='YLS_Peer_Score')
    YLS_Subab_Score = models.IntegerField(db_column='YLS_Subab_Score')
    YLS_Leisure_Score = models.IntegerField(db_column='YLS_Leisure_Score')
    YLS_Personality_Score = models.IntegerField(db_column='YLS_Personality_Score')
    YLS_Attitude_Score = models.IntegerField(db_column='YLS_Attitude_Score')
    Incarcerated_caregivers = models.IntegerField(db_column='Incarcerated_caregivers')
    Incarcerated_siblings = models.IntegerField(db_column='Incarcerated_siblings')
    Number_of_prior_AWOLS = models.IntegerField(db_column='Number_of_prior_AWOLS')
    Animal_cruelty = models.IntegerField(db_column='Animal_cruelty')
    sexually_acting_out_in_past_program = models.IntegerField(db_column='sexually_acting_out_in_past_program')
    prior_hospitalizations = models.IntegerField(db_column='prior_hospitalizations')
    Autism_Diagnosis = models.IntegerField(db_column='Autism_Diagnosis')
    Borderline_Personality = models.IntegerField(db_column='Borderline_Personality')
    Compliant_with_meds = models.IntegerField(db_column='Compliant_with_meds')
    Death_Silblings = models.IntegerField(db_column='Death Silblings') #
    Death_Caregiver = models.IntegerField(db_column='Death_Caregiver')
    Alcohol_Use = models.IntegerField(db_column='Alcohol_Use')
    Drug_Use = models.IntegerField(db_column='Drug_Use')
    Borderline_IQ = models.IntegerField(db_column='Borderline_IQ')
    Significant_mental_health_symptoms = models.IntegerField(db_column='Significant_mental_health_symptoms')
    Severe_mental_health_symptoms = models.IntegerField(db_column='Severe_mental_health_symptoms')
    Number_of_prior_placements = models.IntegerField(db_column='Number_of_prior_placements')
    Psychosis = models.IntegerField(db_column='Psychosis')
    Reactive_Attachment_Disorder = models.IntegerField(db_column='Reactive_Attachment_Disorder')
    Schizophrenia = models.IntegerField(db_column='Schizophrenia')
    Number_of_foster_care_placements = models.IntegerField(db_column='Number_of_foster_care_placements')
    Number_of_prior_treatment_terminations = models.IntegerField(db_column='Number_of_prior_treatment_terminations')
    Length_of_time_since_living_at_home = models.IntegerField(db_column='Length_of_time_since_living_at_home')
    CANS_LifeFunctioning = models.IntegerField(db_column='CANS_LifeFunctioning')
    CANS_YouthStrengths = models.IntegerField(db_column='CANS_YouthStrengths')
    CANS_CareGiverStrengths = models.IntegerField(db_column='CANS_CareGiverStrengths')
    CANS_Culture = models.IntegerField(db_column='CANS_Culture')
    CANS_YouthBehavior = models.IntegerField(db_column='CANS_YouthBehavior')
    CANS_YouthRisk = models.IntegerField(db_column='CANS_YouthRisk')
    CANS_Trauma_Exp = models.IntegerField(db_column='CANS_Trauma_Exp')


class ModelTests(models.Model):
    GENDER_CHOICES = (
        (1, 'Female'),
        (2, "Male")
    )
    RACE_CHOICES = ((1, 'caucasian'),
                    (2, 'African American'),
                    (3, 'Hispanic'),
                    (4, 'Others'))
    LS_CHOICES = ((1, 'voluntary'),
                  (2, 'Dependent'),
                  (3, 'Voluntary Delinquent'),
                  (4, 'Dependent Delinquent'),
                  (5, 'Delinquent'))
    REF_CHOICES = (
        (1, 'Adams'), (2, 'Allegheny'), (3, 'Beaver'), (4, 'Bedford'), (5, 'Berks'),
        (6, 'Blair'), (7, 'Bucks'), (8, 'Butler'), (9, 'Cambria'), (10, 'Centre'), (11, 'Chester'), (12, 'Cumberland'),
        (13, 'Dauphin'), (14, 'Delaware'), (15, 'Erie'), (16, 'Fayette'), (17, 'Franklin'), (18, 'Huntingdon'),
        (19, 'Juniata'),
        (20, 'Kent'), (21, 'Lackawanna'), (22, 'Lancaster'), (23, 'Lebanon'), (24, 'Lehigh'), (25, 'Lycoming'),
        (26, 'Monroe'), (27, 'Montgomery'), (28, 'Montour'), (29, 'Northumberland'), (30, 'Perry'),
        (31, 'Philadelphia'),
        (32, 'Pike'), (34, 'Snyder'), (35, 'Tioga'), (36, 'Washington'), (37, 'Westmoreland'), (38, 'York'),
        (39, 'Armstrong'),
        (40, 'Columbia'), (41, 'Crawford'), (42, 'Cayahoga OH'), (43, 'Franklin OH'), (44, 'Greene'), (45, 'Indiana'),
        (46, 'Lawrence'),
        (47, 'MH'), (48, 'Mckean'), (49, 'Mercer'), (50, 'outside tri-county'), (51, 'Northampton'), (52, 'Pike'),
        (53, 'Schukill'),
        (54, 'Somerset'), (55, 'Union'), (56, 'Venango'))
    CYF_CHOICES = ((1, 'CYF'), (2, 'Juvenile Justice'), (3, 'MH'))
    no_or_yes = ((0, 'no'), (1, 'yes'))
    Termination_av = ((0, 'no'), (1, 'unknown'), (2, 'one'), (3, 'two or more'))
    complaint = ((0, 'no'), (1, 'yes'), (9, 'N / A'))
    prior_awols_choice = ((0, 'none'), (1, 'one'), (2, 'two'), (3, 'many'))
    Borderline_IQ = ((0, '70+, or not listed assumed 70+'), (1, '<70'))
    foster_care_placements = ((0, 'no'), (1, 'one'), (2, 'two'), (3, 'three or more'))
    prior_placements = ((0, 'no'), (1, 'one'), (2, 'two'), (3, 'three or more'))
    Severe_MH_symptoms = ((0, 'no ER/hospitalizations'), (1, 'last 3 months'), (2, '6 months ago'), (3, '9 months ago'),
                          (4, '1 year or more ago'))
    primary_lang_choices = ((1,'English'),(2,'not English'))
    second_lang = ((0,'not at all'),(1,'very little'),(2,'average'),(3,'very well'))

    name = models.CharField(db_column='name', max_length=100)
    dob = models.DateField(db_column='dob')
    client_code = models.IntegerField(db_column='Client_code',primary_key=True)
    gender = models.IntegerField(db_column='Gender', choices=GENDER_CHOICES)
    primaryRaceCode = models.IntegerField(db_column='PrimaryRacecode', choices=RACE_CHOICES)
    ls_type = models.IntegerField(db_column='LS_Type', choices=LS_CHOICES)
    ageAtEpisodeStart = models.IntegerField(db_column='AgeAtEpisodeStart')
    episode_number = models.IntegerField(db_column='EpisodeNumber')
    CYF_code = models.IntegerField(db_column='CYF_code', choices=CYF_CHOICES)
    ageAtEnrollStart = models.IntegerField(db_column='AgeAtEnrollStart')
    RefSourceCode = models.IntegerField(db_column='RefSourceCode', choices=REF_CHOICES)
    termination_directly_to_AV = models.IntegerField(db_column='Termination_directly_to_AV', choices=Termination_av)
    client_self_harm = models.IntegerField(db_column='Client_self_harm')
    yls_PriorCurrentOffenses_Score = models.IntegerField(db_column='YLS_PriorCurrentOffenses_Score',blank=True)
    yls_FamCircumstances_Score = models.IntegerField(db_column='YLS_FamCircumstances_Score',blank=True)
    yls_Edu_Employ_Score = models.IntegerField(db_column='YLS_Edu_Employ_Score',blank=True)
    yls_Peer_Score = models.IntegerField(db_column='YLS_Peer_Score',blank=True)
    yls_Subab_Score = models.IntegerField(db_column='YLS_Subab_Score',blank=True)
    yls_Leisure_Score = models.IntegerField(db_column='YLS_Leisure_Score',blank=True)
    yls_Personality_Score = models.IntegerField(db_column='YLS_Personality_Score',blank=True)
    yls_Attitude_Score = models.IntegerField(db_column='YLS_Attitude_Score',blank=True)
    cans_LifeFunctioning = models.IntegerField(db_column='CANS_LifeFunctioning')
    cans_YouthStrengths = models.IntegerField(db_column='CANS_YouthStrengths')
    cans_CareGiverStrengths = models.IntegerField(db_column='CANS_CareGiverStrengths')
    cans_Culture = models.IntegerField(db_column='CANS_Culture')
    cans_YouthBehavior = models.IntegerField(db_column='CANS_YouthBehavior')
    cans_YouthRisk = models.IntegerField(db_column='CANS_YouthRisk')
    cans_Trauma_Exp = models.IntegerField(db_column='CANS_Trauma_Exp')
    incarcerated_caregivers = models.IntegerField(db_column='Incarcerated_caregivers', choices=no_or_yes)
    incarcerated_siblings = models.IntegerField(db_column='Incarcerated_siblings', choices=no_or_yes)
    number_of_prior_AWOLS = models.IntegerField(db_column='Number_of_prior_AWOLS', choices=prior_awols_choice)
    animal_cruelty = models.IntegerField(db_column='Animal_cruelty', choices=no_or_yes)
    # sexually_acting_out_in_past_program = models.IntegerField(db_column='sexually_acting_out_in_past_program',
    #                                                           choices=SAO_past_program)
    prior_hospitalizations = models.IntegerField(db_column='prior_hospitalizations')
    autism_Diagnosis = models.IntegerField(db_column='Autism_Diagnosis', choices=no_or_yes)
    borderline_Personality = models.IntegerField(db_column='Borderline_Personality', choices=no_or_yes)
    compliant_with_meds = models.IntegerField(db_column='Compliant_with_meds', choices=complaint)
    severe_mental_health_symptoms = models.IntegerField(db_column='Severe_mental_health_symptoms',choices=Severe_MH_symptoms)
    number_of_prior_treatment_terminations = models.IntegerField(db_column='Number_of_prior_treatment_terminations')
    length_of_time_since_living_at_home = models.IntegerField(db_column='Length_of_time_since_living_at_home')
    death_Silblings = models.IntegerField(db_column='Death Silblings', choices=no_or_yes)
    death_Caregiver = models.IntegerField(db_column='Death_Caregiver', choices=no_or_yes)
    alcohol_Use = models.IntegerField(db_column='Alcohol_Use', choices=no_or_yes)
    drug_Use = models.IntegerField(db_column='Drug_Use', choices=no_or_yes)
    borderline_IQ = models.IntegerField(db_column='Borderline_IQ', choices=Borderline_IQ)
    significant_mental_health_symptoms = models.IntegerField(db_column='Significant_mental_health_symptoms')
    number_of_prior_placements = models.IntegerField(db_column='Number_of_prior_placements', choices=prior_placements)
    psychosis = models.IntegerField(db_column='Psychosis', choices=no_or_yes)
    reactive_Attachment_Disorder = models.IntegerField(db_column='Reactive_Attachment_Disorder',
                                                       choices=no_or_yes)
    schizophrenia = models.IntegerField(db_column='Schizophrenia', choices=no_or_yes)
    number_of_foster_care_placements = models.IntegerField(db_column='Number_of_foster_care_placements',
                                                           choices=foster_care_placements)
    modified_date  = models.DateTimeField(db_column='Modified_Date',auto_now=True)


    hist_of_prior_program_SAO = models.IntegerField(db_column='Hist_of_prior_program_SAO',choices=no_or_yes)
    program = models.IntegerField(db_column='Program')
    confidence = models.IntegerField(db_column='Confidence')


    episode_start = models.DateField(db_column='episode_start')
    primary_language = models.IntegerField(db_column='primary_language',choices=primary_lang_choices)
    enrollStart_date = models.DateField(db_column='enrollStart_date')
    english_second_lang = models.IntegerField(db_column='english_second_lang',choices=second_lang)
    level_of_care = models.IntegerField(db_column='level_of_care')
    type_of_drugs = models.TextField(db_column='type_of_drugs')
    family_support = models.IntegerField(db_column='family_support')
    level_of_aggression = models.IntegerField(db_column='level_of_aggression')
    fire_setting = models.IntegerField(db_column='fire_setting')
    abuse_neglect = models.IntegerField(db_column='abuse_neglect',choices=no_or_yes)
    FAST_FamilyTogetherScore = models.IntegerField(db_column='FAST_FamilyTogetherScore')
    FAST_CaregiverAdvocacyScore = models.IntegerField(db_column='FAST_CaregiverAdvocacyScore')
    Screening_tool_Trauma = models.IntegerField(db_column ='Screening_tool_Trauma')




class Ade_Mapping(models.Model):
    program = models.IntegerField(db_column='program')
    gender = models.IntegerField(db_column='gender')
    level_of_care = models.IntegerField(db_column='level_of_care')
    location = ArrayField(models.IntegerField(db_column='location'))
    location_name = ArrayField(models.CharField(db_column='location_name',max_length=100))
    program_name = models.CharField(db_column='program_name',max_length=100)
    level_name = models.CharField(db_column='level_name',max_length=100)


class Adelphoi_Mapping(models.Model):
    program = models.IntegerField(db_column='program')
    program_name = models.CharField(db_column='program_name', max_length=100)

    gender = models.IntegerField(db_column='gender')
    gender_name = models.CharField(db_column='gender_name',max_length=20)

    level_of_care = models.IntegerField(db_column='level_of_care')
    level_names = models.CharField(db_column='level_names', max_length=100)

    location = ArrayField(models.IntegerField(db_column='location'))
    location_names = ArrayField(models.CharField(db_column='location_names',max_length=100))

    facility_type = models.IntegerField(db_column='facility_type')
    facility_names = models.CharField(db_column='facility_names',max_length=100)
