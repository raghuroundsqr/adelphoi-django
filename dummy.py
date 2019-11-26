# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'Adelphoi_Location_mapping'
# The error was: 'NoneType' object is not subscriptable
# Unable to inspect table 'Adelphoi_Mapping'
# The error was: 'NoneType' object is not subscriptable


class FirstmatchModeltest(models.Model):
    ageatenrollstart = models.IntegerField(db_column='AgeAtEnrollStart')  # Field name made lowercase.
    ageatepisodestart = models.IntegerField(db_column='AgeAtEpisodeStart')  # Field name made lowercase.
    alcohol_use = models.IntegerField(db_column='Alcohol_Use')  # Field name made lowercase.
    animal_cruelty = models.IntegerField(db_column='Animal_cruelty')  # Field name made lowercase.
    autism_diagnosis = models.IntegerField(db_column='Autism_Diagnosis')  # Field name made lowercase.
    borderline_iq = models.IntegerField(db_column='Borderline_IQ')  # Field name made lowercase.
    borderline_personality = models.IntegerField(db_column='Borderline_Personality')  # Field name made lowercase.
    cans_caregiverstrengths = models.IntegerField(db_column='CANS_CareGiverStrengths')  # Field name made lowercase.
    cans_culture = models.IntegerField(db_column='CANS_Culture')  # Field name made lowercase.
    cans_lifefunctioning = models.IntegerField(db_column='CANS_LifeFunctioning')  # Field name made lowercase.
    cans_trauma_exp = models.IntegerField(db_column='CANS_Trauma_Exp')  # Field name made lowercase.
    cans_youthbehavior = models.IntegerField(db_column='CANS_YouthBehavior')  # Field name made lowercase.
    cans_youthrisk = models.IntegerField(db_column='CANS_YouthRisk')  # Field name made lowercase.
    cans_youthstrengths = models.IntegerField(db_column='CANS_YouthStrengths')  # Field name made lowercase.
    cyf_code = models.IntegerField(db_column='CYF_code')  # Field name made lowercase.
    client_code = models.IntegerField(db_column='Client_code')  # Field name made lowercase.
    client_self_harm = models.IntegerField(db_column='Client_self_harm')  # Field name made lowercase.
    compliant_with_meds = models.IntegerField(db_column='Compliant_with_meds')  # Field name made lowercase.
    death = models.TextField(db_column='Death')  # Field name made lowercase. This field type is a guess.
    death_caregiver = models.IntegerField(db_column='Death_Caregiver')  # Field name made lowercase.
    drug_use = models.IntegerField(db_column='Drug_Use')  # Field name made lowercase.
    episodenumber = models.IntegerField(db_column='EpisodeNumber')  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    incarcerated_caregivers = models.IntegerField(db_column='Incarcerated_caregivers')  # Field name made lowercase.
    incarcerated_siblings = models.IntegerField(db_column='Incarcerated_siblings')  # Field name made lowercase.
    ls_type = models.IntegerField(db_column='LS_Type')  # Field name made lowercase.
    length_of_time_since_living_at_home = models.IntegerField(db_column='Length_of_time_since_living_at_home')  # Field name made lowercase.
    number_of_foster_care_placements = models.IntegerField(db_column='Number_of_foster_care_placements')  # Field name made lowercase.
    number_of_prior_awols = models.IntegerField(db_column='Number_of_prior_AWOLS')  # Field name made lowercase.
    number_of_prior_placements = models.IntegerField(db_column='Number_of_prior_placements')  # Field name made lowercase.
    number_of_prior_treatment_terminations = models.IntegerField(db_column='Number_of_prior_treatment_terminations')  # Field name made lowercase.
    primaryracecode = models.IntegerField(db_column='PrimaryRacecode')  # Field name made lowercase.
    psychosis = models.IntegerField(db_column='Psychosis')  # Field name made lowercase.
    reactive_attachment_disorder = models.IntegerField(db_column='Reactive_Attachment_Disorder')  # Field name made lowercase.
    refsourcecode = models.IntegerField(db_column='RefSourceCode')  # Field name made lowercase.
    schizophrenia = models.IntegerField(db_column='Schizophrenia')  # Field name made lowercase.
    severe_mental_health_symptoms = models.IntegerField(db_column='Severe_mental_health_symptoms')  # Field name made lowercase.
    significant_mental_health_symptoms = models.IntegerField(db_column='Significant_mental_health_symptoms')  # Field name made lowercase.
    termination_directly_to_av = models.IntegerField(db_column='Termination_directly_to_AV')  # Field name made lowercase.
    yls_attitude_score = models.IntegerField(db_column='YLS_Attitude_Score')  # Field name made lowercase.
    yls_edu_employ_score = models.IntegerField(db_column='YLS_Edu_Employ_Score')  # Field name made lowercase.
    yls_famcircumstances_score = models.IntegerField(db_column='YLS_FamCircumstances_Score')  # Field name made lowercase.
    yls_leisure_score = models.IntegerField(db_column='YLS_Leisure_Score')  # Field name made lowercase.
    yls_peer_score = models.IntegerField(db_column='YLS_Peer_Score')  # Field name made lowercase.
    yls_personality_score = models.IntegerField(db_column='YLS_Personality_Score')  # Field name made lowercase.
    yls_priorcurrentoffenses_score = models.IntegerField(db_column='YLS_PriorCurrentOffenses_Score')  # Field name made lowercase.
    yls_subab_score = models.IntegerField(db_column='YLS_Subab_Score')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)  # AutoField?
    prior_hospitalizations = models.IntegerField()
    sexually_acting_out_in_past_program = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'FirstMatch_modeltest'


class FirstmatchModeltests(models.Model):
    ageatenrollstart = models.IntegerField(db_column='AgeAtEnrollStart')  # Field name made lowercase.
    ageatepisodestart = models.IntegerField(db_column='AgeAtEpisodeStart')  # Field name made lowercase.
    alcohol_use = models.IntegerField(db_column='Alcohol_Use')  # Field name made lowercase.
    animal_cruelty = models.IntegerField(db_column='Animal_cruelty')  # Field name made lowercase.
    autism_diagnosis = models.IntegerField(db_column='Autism_Diagnosis')  # Field name made lowercase.
    borderline_iq = models.IntegerField(db_column='Borderline_IQ')  # Field name made lowercase.
    borderline_personality = models.IntegerField(db_column='Borderline_Personality')  # Field name made lowercase.
    cans_caregiverstrengths = models.IntegerField(db_column='CANS_CareGiverStrengths')  # Field name made lowercase.
    cans_culture = models.IntegerField(db_column='CANS_Culture')  # Field name made lowercase.
    cans_lifefunctioning = models.IntegerField(db_column='CANS_LifeFunctioning')  # Field name made lowercase.
    cans_trauma_exp = models.IntegerField(db_column='CANS_Trauma_Exp')  # Field name made lowercase.
    cans_youthbehavior = models.IntegerField(db_column='CANS_YouthBehavior')  # Field name made lowercase.
    cans_youthrisk = models.IntegerField(db_column='CANS_YouthRisk')  # Field name made lowercase.
    cans_youthstrengths = models.IntegerField(db_column='CANS_YouthStrengths')  # Field name made lowercase.
    cyf_code = models.IntegerField(db_column='CYF_code')  # Field name made lowercase.
    client_code = models.IntegerField(db_column='Client_code')  # Field name made lowercase.
    client_self_harm = models.IntegerField(db_column='Client_self_harm')  # Field name made lowercase.
    compliant_with_meds = models.IntegerField(db_column='Compliant_with_meds')  # Field name made lowercase.
    death = models.TextField(db_column='Death')  # Field name made lowercase. This field type is a guess.
    death_caregiver = models.IntegerField(db_column='Death_Caregiver')  # Field name made lowercase.
    drug_use = models.IntegerField(db_column='Drug_Use')  # Field name made lowercase.
    episodenumber = models.IntegerField(db_column='EpisodeNumber')  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    incarcerated_caregivers = models.IntegerField(db_column='Incarcerated_caregivers')  # Field name made lowercase.
    incarcerated_siblings = models.IntegerField(db_column='Incarcerated_siblings')  # Field name made lowercase.
    ls_type = models.IntegerField(db_column='LS_Type')  # Field name made lowercase.
    length_of_time_since_living_at_home = models.IntegerField(db_column='Length_of_time_since_living_at_home')  # Field name made lowercase.
    number_of_foster_care_placements = models.IntegerField(db_column='Number_of_foster_care_placements')  # Field name made lowercase.
    number_of_prior_awols = models.IntegerField(db_column='Number_of_prior_AWOLS')  # Field name made lowercase.
    number_of_prior_placements = models.IntegerField(db_column='Number_of_prior_placements')  # Field name made lowercase.
    number_of_prior_treatment_terminations = models.IntegerField(db_column='Number_of_prior_treatment_terminations')  # Field name made lowercase.
    primaryracecode = models.IntegerField(db_column='PrimaryRacecode')  # Field name made lowercase.
    psychosis = models.IntegerField(db_column='Psychosis')  # Field name made lowercase.
    reactive_attachment_disorder = models.IntegerField(db_column='Reactive_Attachment_Disorder')  # Field name made lowercase.
    refsourcecode = models.IntegerField(db_column='RefSourceCode')  # Field name made lowercase.
    schizophrenia = models.IntegerField(db_column='Schizophrenia')  # Field name made lowercase.
    severe_mental_health_symptoms = models.IntegerField(db_column='Severe_mental_health_symptoms')  # Field name made lowercase.
    significant_mental_health_symptoms = models.IntegerField(db_column='Significant_mental_health_symptoms')  # Field name made lowercase.
    termination_directly_to_av = models.IntegerField(db_column='Termination_directly_to_AV')  # Field name made lowercase.
    yls_attitude_score = models.IntegerField(db_column='YLS_Attitude_Score')  # Field name made lowercase.
    yls_edu_employ_score = models.IntegerField(db_column='YLS_Edu_Employ_Score')  # Field name made lowercase.
    yls_famcircumstances_score = models.IntegerField(db_column='YLS_FamCircumstances_Score')  # Field name made lowercase.
    yls_leisure_score = models.IntegerField(db_column='YLS_Leisure_Score')  # Field name made lowercase.
    yls_peer_score = models.IntegerField(db_column='YLS_Peer_Score')  # Field name made lowercase.
    yls_personality_score = models.IntegerField(db_column='YLS_Personality_Score')  # Field name made lowercase.
    yls_priorcurrentoffenses_score = models.IntegerField(db_column='YLS_PriorCurrentOffenses_Score')  # Field name made lowercase.
    yls_subab_score = models.IntegerField(db_column='YLS_Subab_Score')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)  # AutoField?
    prior_hospitalizations = models.IntegerField()
    sexually_acting_out_in_past_program = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'FirstMatch_modeltests'


class FirstmatchModeltestsub(models.Model):
    program = models.IntegerField(db_column='Program')  # Field name made lowercase.
    modeltests_ptr_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'FirstMatch_modeltestsub'


class FirstmatchTestmodels(models.Model):
    gender = models.CharField(db_column='Gender')  # Field name made lowercase.
    ls_type = models.CharField(db_column='LS_Type')  # Field name made lowercase.
    primaryracecode = models.CharField(db_column='PrimaryRacecode')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'FirstMatch_testmodels'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    codename = models.CharField()
    content_type_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    date_joined = models.DateTimeField()
    email = models.CharField()
    first_name = models.CharField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    last_name = models.CharField()
    password = models.CharField()
    username = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    group_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    permission_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_flag = models.IntegerField()
    action_time = models.DateTimeField()
    change_message = models.CharField()
    content_type_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.CharField()
    object_repr = models.CharField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    model = models.CharField()
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField()
    applied = models.DateTimeField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    expire_date = models.DateTimeField()
    session_data = models.CharField()
    session_key = models.CharField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'django_session'


class Student(models.Model):
    first_name = models.CharField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    last_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'student'
