from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Create your models here.
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





class TestMod(models.Model):
    Client_code = models.IntegerField(db_column='Client_code', blank=True, null=True)
    prior_hospitalizations = models.IntegerField(db_column='prior_hospitalizations', blank=True, null=True)
    class Meta:
        db_table = "TestMod"

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=30)
    class Meta:
        db_table = "student"


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


# class FirstmatchTestmodels(models.Model):
#     gender = models.CharField(db_column='Gender',max_length=20)  # Field name made lowercase.
#     ls_type = models.CharField(db_column='LS_Type',max_length=20)  # Field name made lowercase.
#     primaryracecode = models.CharField(db_column='PrimaryRacecode',max_length=20)  # Field name made lowercase.
#     # id = models.IntegerField(primary_key=True)  # AutoField?
#
#     class Meta:
#         managed = False
#         db_table = 'FirstMatch_testmodels'

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
    caregivers_choice = ((0, 'no'), (1, 'yes'))
    cruelty_choice = ((0, 'no'), (1, 'yes'))
    Termination_av = ((0, 'no'), (1, 'unknown'), (2, 'one'), (3, 'two or more'))
    Autism = ((0, 'no'), (1, 'yes'))
    complaint = ((0, 'no'), (1, 'yes'), (9, 'N / A'))
    inc_siblings_choice = ((0, 'no'), (1, 'yes'))
    border_per = ((0, 'no'), (1, 'yes'))
    prior_awols_choice = ((0, 'none'), (1, 'one'), (2, 'two'), (3, 'many'))
    SAO_past_program = ((0, 'no'), (1, 'yes'))
    Borderline_IQ = ((0, '70+, or not listed assumed 70+'), (1, '<70'))
    foster_care_placements = ((0, 'no'), (1, 'one'), (2, 'two'), (3, 'three or more'))
    prior_placements = ((0, 'no'), (1, 'one'), (2, 'two'), (3, 'three or more'))
    Death_Caregiver = ((0, 'no'), (1, 'yes'))
    Death_Silblings = ((0, 'no'), (1, 'yes'))
    Alcohol_Use = ((0, 'no'), (1, 'yes'))
    Drug_Use = ((0, 'no'), (1, 'yes'))
    Psychosis = ((0, 'no'), (1, 'yes'))
    Reactive_Attachment_Disorder = ((0, 'no'), (1, 'yes'))
    Schizophrenia = ((0, 'no'), (1, 'yes'))
    Severe_MH_symptoms = ((0, 'no ER/hospitalizations'), (1, 'last 3 months'), (2, '6 months ago'), (3, '9 months ago'),
                          (4, '1 year or more ago'))

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
    incarcerated_caregivers = models.IntegerField(db_column='Incarcerated_caregivers', choices=caregivers_choice)
    incarcerated_siblings = models.IntegerField(db_column='Incarcerated_siblings', choices=inc_siblings_choice)
    number_of_prior_AWOLS = models.IntegerField(db_column='Number_of_prior_AWOLS', choices=prior_awols_choice)
    animal_cruelty = models.IntegerField(db_column='Animal_cruelty', choices=cruelty_choice)
    # sexually_acting_out_in_past_program = models.IntegerField(db_column='sexually_acting_out_in_past_program',
    #                                                           choices=SAO_past_program)
    prior_hospitalizations = models.IntegerField(db_column='prior_hospitalizations')
    autism_Diagnosis = models.IntegerField(db_column='Autism_Diagnosis', choices=Autism)
    borderline_Personality = models.IntegerField(db_column='Borderline_Personality', choices=border_per)
    compliant_with_meds = models.IntegerField(db_column='Compliant_with_meds', choices=complaint)
    severe_mental_health_symptoms = models.IntegerField(db_column='Severe_mental_health_symptoms',choices=Severe_MH_symptoms)
    number_of_prior_treatment_terminations = models.IntegerField(db_column='Number_of_prior_treatment_terminations')
    length_of_time_since_living_at_home = models.IntegerField(db_column='Length_of_time_since_living_at_home')
    death_Silblings = models.IntegerField(db_column='Death Silblings', choices=Death_Silblings)
    death_Caregiver = models.IntegerField(db_column='Death_Caregiver', choices=Death_Caregiver)
    alcohol_Use = models.IntegerField(db_column='Alcohol_Use', choices=Alcohol_Use)
    drug_Use = models.IntegerField(db_column='Drug_Use', choices=Drug_Use)
    borderline_IQ = models.IntegerField(db_column='Borderline_IQ', choices=Borderline_IQ)
    significant_mental_health_symptoms = models.IntegerField(db_column='Significant_mental_health_symptoms')
    number_of_prior_placements = models.IntegerField(db_column='Number_of_prior_placements', choices=prior_placements)
    psychosis = models.IntegerField(db_column='Psychosis', choices=Psychosis)
    reactive_Attachment_Disorder = models.IntegerField(db_column='Reactive_Attachment_Disorder',
                                                       choices=Reactive_Attachment_Disorder)
    schizophrenia = models.IntegerField(db_column='Schizophrenia', choices=Schizophrenia)
    number_of_foster_care_placements = models.IntegerField(db_column='Number_of_foster_care_placements',
                                                           choices=foster_care_placements)
    modified_date  = models.DateTimeField(db_column='Modified_Date',auto_now=True)


    hist_of_prior_program_SAO = models.IntegerField(db_column='Hist_of_prior_program_SAO',choices=SAO_past_program)
    program = models.IntegerField(db_column='Program')
    confidence = models.IntegerField(db_column='Confidence')

# class ModelTestSub(ModelTests):
#     program = models.IntegerField(db_column='Program', default=999)
    # confidence = models.IntegerField(db_column='Confidence', default=999)

class FirstmatchAdelphoiMapping2(models.Model):
    gender = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    level = models.TextField()  # This field type is a guess.
    location = models.TextField()  # This field type is a guess.
    program = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'FirstMatch_adelphoi_mapping2'