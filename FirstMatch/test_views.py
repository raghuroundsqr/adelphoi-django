# Create your views here.
import json
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import TestModels, ModelTests, Ade_Mapping, Adelphoi_Mapping  # ,Mapping_Collection  #,ModelTestSub
from django.views.decorators.csrf import csrf_exempt
from .forms import TestForms, TestForms2, ModelTestForms
# from django.views import View
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
import pandas as pd
import numpy as np
import pickle
from rest_framework.parsers import JSONParser
###

from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ModelTestsSerializers, ModelTestsSerializers_selected_program, \
    ModelTestsSerializer_program_model_suggested, ProgramSerialzer, LocationSerialzer, ProgramLocationSerialzer, \
    ProgramLevelSerialzer, FilterSerialzer
from rest_framework.parsers import JSONParser
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend


@csrf_exempt
def adelphoi_insert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Client_code = data["Client_code"]
        Gender = data["Gender"]
        PrimaryRacecode = data["PrimaryRacecode"]
        LS_Type = data["LS_Type"]
        AgeAtEpisodeStart = data["AgeAtEpisodeStart"]
        EpisodeNumber = data["EpisodeNumber"]
        CYF_code = data["CYF_code"]
        AgeAtEnrollStart = data["AgeAtEnrollStart"]
        RefSourceCode = data["RefSourceCode"]
        Incarcerated_caregivers = data["Incarcerated_caregivers"]
        Incarcerated_siblings = data["Incarcerated_siblings"]
        Number_of_prior_AWOLS = data["Number_of_prior_AWOLS"]
        Animal_cruelty = data["Animal_cruelty"]
        sexually_acting_out_in_past_program = data["sexually_acting_out_in_past_program"]
        prior_hospitalizations = data["prior_hospitalizations"]
        Termination_directly_to_AV = data["Termination_directly_to_AV"]
        Autism_Diagnosis = data["Autism_Diagnosis"]
        Borderline_Personality = data["Borderline_Personality"]
        Compliant_with_meds = data["Compliant_with_meds"]

        query = TestModels.objects.filter(Client_code=Client_code).values()
        # checking for client exists or not.
        if query.count() > 0:
            print("Client_code already exists")
            # TestModels.objects.filter(Client_code=Client_code).update(Gender = Gender)
            for i in query:
                Client_code = i["Client_code"]
                Gender = i["Gender"]
                PrimaryRacecode = i["PrimaryRacecode"]
                LS_Type = i["LS_Type"]
                AgeAtEpisodeStart = i["AgeAtEpisodeStart"]
                EpisodeNumber = i["EpisodeNumber"]
                CYF_code = i["CYF_code"]
                AgeAtEnrollStart = i["AgeAtEnrollStart"]
                RefSourceCode = i["RefSourceCode"]
                Incarcerated_caregivers = i["Incarcerated_caregivers"]
                Incarcerated_siblings = i["Incarcerated_siblings"]
                Number_of_prior_AWOLS = i["Number_of_prior_AWOLS"]
                Animal_cruelty = i["Animal_cruelty"]
                sexually_acting_out_in_past_program = i["sexually_acting_out_in_past_program"]
                prior_hospitalizations = i["prior_hospitalizations"]
                Termination_directly_to_AV = i["Termination_directly_to_AV"]
                Autism_Diagnosis = i["Autism_Diagnosis"]
                Borderline_Personality = i["Borderline_Personality"]
                Compliant_with_meds = i["Compliant_with_meds"]

                data = {"Client_code": Client_code, "Gender": Gender, "PrimaryRacecode": PrimaryRacecode,
                        "LS_Type": LS_Type, "AgeAtEpisodeStart": AgeAtEpisodeStart,
                        "EpisodeNumber": EpisodeNumber, "CYF_code": CYF_code, "AgeAtEnrollStart": AgeAtEnrollStart,
                        "RefSourceCode": RefSourceCode, "Incarcerated_caregivers": Incarcerated_caregivers,
                        "Incarcerated_siblings": Incarcerated_siblings, "Number_of_prior_AWOLS": Number_of_prior_AWOLS,
                        "Animal_cruelty": Animal_cruelty,
                        "sexually_acting_out_in_past_program": sexually_acting_out_in_past_program,
                        "Autism_Diagnosis": Autism_Diagnosis,
                        "prior_hospitalizations": prior_hospitalizations,
                        "Termination_directly_to_AV": Termination_directly_to_AV,
                        "Borderline_Personality": Borderline_Personality,
                        "Compliant_with_meds": Compliant_with_meds}

                return JsonResponse({'Message': "Client code already exists", 'data': data, 'success': 1,
                                     'message': 'data retrieved successfully'})

        else:
            print("new Client_code")
            aa = TestModels(Client_code=Client_code, Gender=Gender, PrimaryRacecode=PrimaryRacecode, LS_Type=LS_Type,
                            AgeAtEpisodeStart=AgeAtEpisodeStart,
                            EpisodeNumber=EpisodeNumber, CYF_code=CYF_code, AgeAtEnrollStart=AgeAtEnrollStart,
                            RefSourceCode=RefSourceCode,
                            Incarcerated_caregivers=Incarcerated_caregivers,
                            Incarcerated_siblings=Incarcerated_siblings, Number_of_prior_AWOLS=Number_of_prior_AWOLS,
                            Animal_cruelty=Animal_cruelty,
                            sexually_acting_out_in_past_program=sexually_acting_out_in_past_program,
                            prior_hospitalizations=prior_hospitalizations,
                            Termination_directly_to_AV=Termination_directly_to_AV,
                            Autism_Diagnosis=Autism_Diagnosis, Borderline_Personality=Borderline_Personality,
                            Compliant_with_meds=Compliant_with_meds)

            aa.save()
            return JsonResponse({'message': 'Insertion is done successfully', 'success': 1})
    else:
        return JsonResponse({'message': 'Method not allowed', 'success': 0})


class AboutView(TemplateView):
    template_name = 'success.html'


class CBView(CreateView):
    form_class = TestForms
    template_name = 'ad_index.html'


class ModelView(CreateView):
    form_class = ModelTestForms
    template_name = 'ad_index.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            # - Insert data to AI model
            client_code = form.cleaned_data.get('client_code')
            gender = form.cleaned_data.get('gender')
            primaryRaceCode = form.cleaned_data.get('primaryRaceCode')
            ls_type = form.cleaned_data.get('ls_type')
            ageAtEpisodeStart = form.cleaned_data.get('ageAtEpisodeStart')
            episode_number = form.cleaned_data.get('episode_number')
            CYF_code = form.cleaned_data.get('CYF_code')
            # ageAtEnrollStart = form.cleaned_data.get('ageAtEnrollStart')
            RefSourceCode = form.cleaned_data.get('RefSourceCode')
            termination_directly_to_AV = form.cleaned_data.get('termination_directly_to_AV')
            client_self_harm = form.cleaned_data.get('client_self_harm')
            yls_PriorCurrentOffenses_Score = form.cleaned_data.get('yls_PriorCurrentOffenses_Score')
            yls_FamCircumstances_Score = form.cleaned_data.get('yls_FamCircumstances_Score')
            yls_Edu_Employ_Score = form.cleaned_data.get('yls_Edu_Employ_Score')
            yls_Peer_Score = form.cleaned_data.get('yls_Peer_Score')
            yls_Subab_Score = form.cleaned_data.get('yls_Subab_Score')
            yls_Leisure_Score = form.cleaned_data.get('yls_Leisure_Score')
            yls_Personality_Score = form.cleaned_data.get('yls_Personality_Score')
            yls_Attitude_Score = form.cleaned_data.get('yls_Attitude_Score')
            cans_LifeFunctioning = form.cleaned_data.get('cans_LifeFunctioning')
            cans_YouthStrengths = form.cleaned_data.get('cans_YouthStrengths')
            cans_CareGiverStrengths = form.cleaned_data.get('cans_CareGiverStrengths')
            cans_Culture = form.cleaned_data.get('cans_Culture')
            cans_YouthBehavior = form.cleaned_data.get('cans_YouthBehavior')
            cans_YouthRisk = form.cleaned_data.get('cans_YouthRisk')
            cans_Trauma_Exp = form.cleaned_data.get('cans_Trauma_Exp')
            incarcerated_caregivers = form.cleaned_data.get('incarcerated_caregivers')
            incarcerated_siblings = form.cleaned_data.get('incarcerated_siblings')
            number_of_prior_AWOLS = form.cleaned_data.get('number_of_prior_AWOLS')
            animal_cruelty = form.cleaned_data.get('animal_cruelty')
            hist_of_prior_program_SAO = form.cleaned_data.get('hist_of_prior_program_SAO')
            prior_hospitalizations = form.cleaned_data.get('prior_hospitalizations')
            autism_Diagnosis = form.cleaned_data.get('autism_Diagnosis')
            borderline_Personality = form.cleaned_data.get('borderline_Personality')
            compliant_with_meds = form.cleaned_data.get('compliant_with_meds')
            severe_mental_health_symptoms = form.cleaned_data.get('severe_mental_health_symptoms')
            number_of_prior_treatment_terminations = form.cleaned_data.get('number_of_prior_treatment_terminations')
            length_of_time_since_living_at_home = form.cleaned_data.get('length_of_time_since_living_at_home')
            death_Silblings = form.cleaned_data.get('death_Silblings')
            death_Caregiver = form.cleaned_data.get('death_Caregiver')
            alcohol_Use = form.cleaned_data.get('alcohol_Use')
            drug_Use = form.cleaned_data.get('drug_Use')
            borderline_IQ = form.cleaned_data.get('borderline_IQ')
            significant_mental_health_symptoms = form.cleaned_data.get('significant_mental_health_symptoms')
            number_of_prior_placements = form.cleaned_data.get('number_of_prior_placements')
            psychosis = form.cleaned_data.get('psychosis')
            reactive_Attachment_Disorder = form.cleaned_data.get('reactive_Attachment_Disorder')
            schizophrenia = form.cleaned_data.get('schizophrenia')
            number_of_foster_care_placements = form.cleaned_data.get('number_of_foster_care_placements')

            episode_start = form.cleaned_data.get('episode_start')
            primary_language = form.cleaned_data.get('primary_language')
            enrollStart_date = form.cleaned_data.get('enrollStart_date')
            english_second_lang = form.cleaned_data.get('english_second_lang')
            type_of_drugs = form.cleaned_data.get('type_of_drugs')
            family_support = form.cleaned_data.get('family_support')
            level_of_aggression = form.cleaned_data.get('level_of_aggression')
            fire_setting = form.cleaned_data.get('fire_setting')
            abuse_neglect = form.cleaned_data.get('abuse_neglect')
            FAST_FamilyTogetherScore = form.cleaned_data.get('FAST_FamilyTogetherScore')
            FAST_CaregiverAdvocacyScore = form.cleaned_data.get('FAST_CaregiverAdvocacyScore')
            Screening_tool_Trauma = form.cleaned_data.get('Screening_tool_Trauma')

            print(client_code)

            dt = {'Gender': gender, 'PrimaryRacecode': primaryRaceCode, 'CYF_code': CYF_code, 'LS_Type': ls_type,
                  'EpisodeNumber': episode_number,
                  'RefSourceName': RefSourceCode, 'Number of foster care placements': number_of_foster_care_placements,
                  'AgeAtEpisodeStart': ageAtEpisodeStart,
                  'Number of prior placements \n(excluding shelter and detention)': number_of_prior_placements,
                  'Number of prior treatment terminations (excluding shelter or detention)': number_of_prior_treatment_terminations,
                  'Length of time since living at home': length_of_time_since_living_at_home,
                  'Termination directly to AV': termination_directly_to_AV,
                  'Death Caregiver': death_Caregiver, 'Borderline IQ (below 70)': borderline_IQ,
                  'Hist of prior program SAO': hist_of_prior_program_SAO,  # hist_of_prior_program_SAO
                  'Death Silblings': death_Silblings, 'Alcohol Use': alcohol_Use, 'Drug Use': drug_Use,
                  'Incarcerated caregivers': incarcerated_caregivers,
                  'Incarcerated siblings': incarcerated_siblings, 'Number of prior AWOLS': number_of_prior_AWOLS,
                  'Animal cruelty': animal_cruelty,
                  'Number of prior hospitalizations': prior_hospitalizations,
                  'Compliant with medication': compliant_with_meds,
                  'Significant mental health symptoms': significant_mental_health_symptoms,
                  'Severe mental health symptoms': severe_mental_health_symptoms,
                  'Autism Diagnosis': autism_Diagnosis, 'Borderline Personality': borderline_Personality,
                  'Psychosis': psychosis,
                  'Reactive Attachment Disorder': reactive_Attachment_Disorder, 'Schizophrenia': schizophrenia,
                  'YLS_PriorCurrentOffenses_Score': yls_PriorCurrentOffenses_Score,
                  'YLS_FamCircumstances_Score': yls_FamCircumstances_Score,
                  'YLS_Edu_Employ_Score': yls_Edu_Employ_Score, 'YLS_Peer_Score': yls_Peer_Score,
                  'YLS_Subab_Score': yls_Subab_Score,
                  'YLS_Leisure_Score': yls_Leisure_Score, 'YLS_Personality_Score': yls_Personality_Score,
                  'YLS_Attitude_Score': yls_Attitude_Score, 'Client self-harm': client_self_harm,

                  'CANS_LifeFunctioning': cans_LifeFunctioning,
                  'CANS_YouthStrengths': cans_YouthStrengths, 'CANS_CareGiverStrengths': cans_CareGiverStrengths,
                  'CANS_Culture': cans_Culture,
                  'CANS_YouthBehavior': cans_YouthBehavior, 'CANS_YouthRisk': cans_YouthRisk,
                  'CANS_Trauma_Exp': cans_Trauma_Exp,
                  'Family support': family_support, 'Level of aggression': level_of_aggression,
                  'Fire setting': fire_setting,
                  'Abuse, or neglect': abuse_neglect, 'Screening tool for Trauma--Total score': Screening_tool_Trauma
                  }  # 'AgeAtEnrollStart': ageAtEnrollStart,

            data = pd.DataFrame(dt, index=[0])
            print(data.columns)
            print(data.shape)
            print(data)

            # du = data[['Gender','PrimaryRacecode','LS_Type','CYF code','RefSourceName']]
            # print(du)
            # dd = pd.get_dummies(du,prefix_sep='_',drop_first=True)
            # print(dd)

            Feature_names = ['EpisodeNumber', 'Number of foster care placements', 'AgeAtEpisodeStart',
                             'Number of prior placements \n(excluding shelter and detention)',
                             'Number of prior treatment terminations (excluding shelter or detention)',
                             'Length of time since living at home', 'Termination directly to AV',
                             'Death Caregiver', 'Borderline IQ (below 70)', 'Hist of prior program SAO',
                             'Death Silblings', 'Alcohol Use', 'Drug Use', 'Incarcerated caregivers',
                             'Incarcerated siblings', 'Number of prior AWOLS', 'Animal cruelty',
                             'Number of prior hospitalizations', 'Compliant with medication',
                             'Significant mental health symptoms', 'Severe mental health symptoms',
                             'Autism Diagnosis', 'Borderline Personality', 'Psychosis',
                             'Reactive Attachment Disorder', 'Schizophrenia', 'YLS_PriorCurrentOffenses_Score',
                             'YLS_FamCircumstances_Score',
                             'YLS_Edu_Employ_Score', 'YLS_Peer_Score', 'YLS_Subab_Score',
                             'YLS_Leisure_Score', 'YLS_Personality_Score', 'YLS_Attitude_Score', 'Client self-harm',
                             'CANS_LifeFunctioning',
                             'CANS_YouthStrengths', 'CANS_CareGiverStrengths', 'CANS_Culture',
                             'CANS_YouthBehavior', 'CANS_YouthRisk', 'CANS_Trauma_Exp', 'Family support',
                             'Level of aggression', 'Fire setting',
                             'Abuse, or neglect', 'Screening tool for Trauma--Total score']  # 'AgeAtEnrollStart',

            print("features::", data[Feature_names].shape)
            dummies = pd.DataFrame()
            print("dummies shape", dummies.shape)

            for column in ['Gender', 'PrimaryRacecode', 'LS_Type', 'CYF_code', 'RefSourceName']:
                dummies1 = pd.get_dummies(data[column], prefix=column)
                dummies[dummies1.columns] = dummies1.copy(deep=False)
            print("data columns head", (data[column]).head())
            print("data columns shape", (data[column]).shape)

            print("dummies1 shape", dummies1.shape)

            cols = ['Gender_1', 'Gender_2', 'PrimaryRacecode_1', 'PrimaryRacecode_2',
                    'PrimaryRacecode_3', 'LS_Type_1', 'LS_Type_2', 'LS_Type_4', 'LS_Type_5',
                    'CYF_code_1', 'CYF_code_2', 'RefSourceName_1', 'RefSourceName_2',
                    'RefSourceName_3', 'RefSourceName_4', 'RefSourceName_5',
                    'RefSourceName_6', 'RefSourceName_7', 'RefSourceName_8',
                    'RefSourceName_12', 'RefSourceName_13', 'RefSourceName_14',
                    'RefSourceName_15', 'RefSourceName_16', 'RefSourceName_17',
                    'RefSourceName_18', 'RefSourceName_22', 'RefSourceName_24',
                    'RefSourceName_25', 'RefSourceName_26', 'RefSourceName_31',
                    'RefSourceName_35', 'RefSourceName_36', 'RefSourceName_37',
                    'RefSourceName_38', 'RefSourceName_39', 'RefSourceName_41',
                    'RefSourceName_42', 'RefSourceName_43', 'RefSourceName_45',
                    'RefSourceName_46', 'RefSourceName_48', 'RefSourceName_49',
                    'RefSourceName_51', 'RefSourceName_52', 'RefSourceName_54']

            for col in cols:
                if col in dummies.columns:
                    print('present', col)
                else:
                    dummies[col] = 0

            dummies.drop(["RefSourceName_27"], axis=1, inplace=True)

            print("dummies shape", dummies.shape)
            print(("dumm", dummies.columns))
            Xtest = data[Feature_names]
            Xtest[dummies.columns] = dummies
            Xtest.shape
            print("xtest colimns", Xtest.columns)
            ### LR JOY
            # data = data.fillna(0,inplace=True)  # remove in front end
            # pre-processing
            #
            # dummies  = pd.DataFrame()
            # for column in du:
            #     dummies1 = pd.get_dummies(data[column],prefix=column)
            #     dummies[dummies1.columns] = dummies1.copy(deep=False)
            #
            # print(dummies)

            level_model = pickle.load(open("/home/ubuntu/Adelphoi/adelphoi-django/sources/dt_LR_Level_0.1.sav",
                                           "rb"))  # final_dt_48p_263r_2clases_smote.sav
            program_model = pickle.load(open("/home/ubuntu/Adelphoi/adelphoi-django/sources/dt_T_Program.sav", "rb"))

            # results = loaded_model.predict_proba(data)
            # print("results::", results)
            level_pred = level_model.predict(Xtest)
            program_pred = program_model.predict(Xtest)
            print(level_pred)
            print("program", program_pred)

            # Program_suggested = np.argmax(results[0]) + 1
            # Confidence = results[0][Program_suggested - 1]
            query = Ade_Mapping.objects.filter(program=program_pred, gender=gender, level_of_care=level_pred)
            location_list = []
            program_list = []
            level_list = []
            for i in query:
                program_list.append(i.program_name)
                level_list.append(i.level_name)
                location_list.append(i.location_name)
            # print(f'Model is suggesting Program - {str(Program_suggested)} with confidence of {str(round(Confidence * 100, 2))}')
            # result = (f'Model is suggesting Program - {str(Program_suggested)} locations are {location_list}') #\n with confidence of {str(round(Confidence * 100, 2))}
            result = (
                f'Model is suggesting Program - {program_list} -------\t level of care---{level_list}------- locations are {location_list}')  # \n with confidence of {str(round(Confidence * 100, 2))}

            # result = (f'Model is suggesting Program - {str(program_pred)} \t level of care---{str(level_pred)} locations are {location_list}')  # \n with confidence of {str(round(Confidence * 100, 2))}

            p = ModelTests(client_code=client_code, gender=gender, primaryRaceCode=primaryRaceCode, ls_type=ls_type,
                           ageAtEpisodeStart=ageAtEpisodeStart, episode_number=episode_number, CYF_code=CYF_code,
                           ageAtEnrollStart=ageAtEnrollStart,
                           RefSourceCode=RefSourceCode, termination_directly_to_AV=termination_directly_to_AV,
                           client_self_harm=client_self_harm,
                           yls_PriorCurrentOffenses_Score=yls_PriorCurrentOffenses_Score,
                           yls_FamCircumstances_Score=yls_FamCircumstances_Score,
                           yls_Edu_Employ_Score=yls_Edu_Employ_Score, yls_Peer_Score=yls_Peer_Score,
                           yls_Subab_Score=yls_Subab_Score, yls_Leisure_Score=yls_Leisure_Score,
                           yls_Personality_Score=yls_Personality_Score, yls_Attitude_Score=yls_Attitude_Score,
                           cans_LifeFunctioning=cans_LifeFunctioning, cans_YouthStrengths=cans_YouthStrengths,
                           cans_CareGiverStrengths=cans_CareGiverStrengths,
                           cans_Culture=cans_Culture, cans_YouthBehavior=cans_YouthBehavior,
                           cans_YouthRisk=cans_YouthRisk, cans_Trauma_Exp=cans_Trauma_Exp,
                           incarcerated_caregivers=incarcerated_caregivers, incarcerated_siblings=incarcerated_siblings,
                           number_of_prior_AWOLS=number_of_prior_AWOLS,
                           animal_cruelty=animal_cruelty, hist_of_prior_program_SAO=hist_of_prior_program_SAO,
                           prior_hospitalizations=prior_hospitalizations,
                           autism_Diagnosis=autism_Diagnosis, borderline_Personality=borderline_Personality,
                           compliant_with_meds=compliant_with_meds,
                           severe_mental_health_symptoms=severe_mental_health_symptoms,
                           number_of_prior_treatment_terminations=number_of_prior_treatment_terminations,
                           length_of_time_since_living_at_home=length_of_time_since_living_at_home,
                           death_Silblings=death_Silblings, death_Caregiver=death_Caregiver, alcohol_Use=alcohol_Use,
                           drug_Use=drug_Use, borderline_IQ=borderline_IQ,
                           significant_mental_health_symptoms=significant_mental_health_symptoms,
                           number_of_prior_placements=number_of_prior_placements, psychosis=psychosis,
                           reactive_Attachment_Disorder=reactive_Attachment_Disorder, schizophrenia=schizophrenia,
                           number_of_foster_care_placements=number_of_foster_care_placements,

                           level_of_care=level_pred, episode_start=episode_start, primary_language=primary_language,
                           enrollStart_date=enrollStart_date,
                           english_second_lang=english_second_lang, type_of_drugs=type_of_drugs,
                           family_support=family_support, FAST_FamilyTogetherScore=FAST_FamilyTogetherScore,
                           FAST_CaregiverAdvocacyScore=FAST_CaregiverAdvocacyScore, fire_setting=fire_setting,
                           abuse_neglect=abuse_neglect,
                           Screening_tool_Trauma=Screening_tool_Trauma, level_of_aggression=level_of_aggression,

                           program=level_pred)  # program = Program_suggested,confidence = Confidence

            p.save()
            return HttpResponse(result)
        else:
            form.errors()

            #############
            # - Get predicted values
            # - insert to xxx model
            # if predication is not good:
            #     return HttpResponseRedirect()

        return super().post(request, *args, **kwargs)

    # def get_form(self):
    #     form = super(ModelView,self).get_form()
    #     print(form['Client_code'])


class AdelphoiList(ListCreateAPIView):
    serializer_class = ModelTestsSerializers
    # serializer_class =  ModelTestsSerializers_selected_program
    queryset = ModelTests.objects.all()

    def get(self, request):
        return Response("Success")

    def post(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data.get('Exclusionary_Criteria') == True:
            dt = {'Gender': serializer.validated_data.get('gender'),
                  'PrimaryRacecode': serializer.validated_data.get('primaryRaceCode'),
                  'AgeAtEnrollStart': serializer.validated_data.get('ageAtEnrollStart'),
                  'CYF_code': serializer.validated_data.get('CYF_code'),
                  'LS_Type': serializer.validated_data.get('ls_type'),
                  'EpisodeNumber': serializer.validated_data.get('episode_number'),
                  'RefSourceName': serializer.validated_data.get('RefSourceCode'),
                  'Number of foster care placements': serializer.validated_data.get('number_of_foster_care_placements'),
                  'AgeAtEpisodeStart': serializer.validated_data.get('ageAtEpisodeStart'),
                  'Number of prior placements \n(excluding shelter and detention)': serializer.validated_data.get(
                      'number_of_prior_placements'),
                  'Number of prior treatment terminations (excluding shelter or detention)': serializer.validated_data.get(
                      'number_of_prior_treatment_terminations'),
                  'Length of time since living at home': serializer.validated_data.get(
                      'length_of_time_since_living_at_home'),
                  'Termination directly to AV': serializer.validated_data.get('termination_directly_to_AV'),
                  'Death Caregiver': serializer.validated_data.get('death_Caregiver'),
                  'Borderline IQ (below 70)': serializer.validated_data.get('borderline_IQ'),
                  'Hist of prior program SAO': serializer.validated_data.get('hist_of_prior_program_SAO'),
                  'Death Silblings': serializer.validated_data.get('death_Silblings'),
                  'Alcohol Use': serializer.validated_data.get('alcohol_Use'),
                  'Drug Use': serializer.validated_data.get('drug_Use'),
                  'Incarcerated caregivers': serializer.validated_data.get('incarcerated_caregivers'),
                  'Incarcerated siblings': serializer.validated_data.get('incarcerated_siblings'),
                  'Number of prior AWOLS': serializer.validated_data.get('number_of_prior_AWOLS'),
                  'Animal cruelty': serializer.validated_data.get('animal_cruelty'),
                  'Number of prior hospitalizations': serializer.validated_data.get('prior_hospitalizations'),
                  'Compliant with medication': serializer.validated_data.get('compliant_with_meds'),
                  'Significant mental health symptoms': serializer.validated_data.get(
                      'significant_mental_health_symptoms'),
                  'Severe mental health symptoms': serializer.validated_data.get('severe_mental_health_symptoms'),
                  'Autism Diagnosis': serializer.validated_data.get('autism_Diagnosis'),
                  'Borderline Personality': serializer.validated_data.get('borderline_Personality'),
                  'Psychosis': serializer.validated_data.get('psychosis'),
                  'Reactive Attachment Disorder': serializer.validated_data.get('reactive_Attachment_Disorder'),
                  'Schizophrenia': serializer.validated_data.get('schizophrenia'),
                  'YLS_PriorCurrentOffenses_Score': serializer.validated_data.get('yls_PriorCurrentOffenses_Score'),
                  'YLS_FamCircumstances_Score': serializer.validated_data.get('yls_FamCircumstances_Score'),
                  'YLS_Edu_Employ_Score': serializer.validated_data.get('yls_Edu_Employ_Score'),
                  'YLS_Peer_Score': serializer.validated_data.get('yls_Peer_Score'),
                  'YLS_Subab_Score': serializer.validated_data.get('yls_Subab_Score'),
                  'YLS_Leisure_Score': serializer.validated_data.get('yls_Leisure_Score'),
                  'YLS_Personality_Score': serializer.validated_data.get('yls_Personality_Score'),
                  'YLS_Attitude_Score': serializer.validated_data.get('yls_Attitude_Score'),
                  'Client self-harm': serializer.validated_data.get('client_self_harm'),

                  'CANS_LifeFunctioning': serializer.validated_data.get('cans_LifeFunctioning'),
                  'CANS_YouthStrengths': serializer.validated_data.get('cans_YouthStrengths'),
                  'CANS_CareGiverStrengths': serializer.validated_data.get('cans_CareGiverStrengths'),
                  'CANS_Culture': serializer.validated_data.get('cans_Culture'),
                  'CANS_YouthBehavior': serializer.validated_data.get('cans_YouthBehavior'),
                  'CANS_YouthRisk': serializer.validated_data.get('cans_YouthRisk'),
                  'CANS_Trauma_Exp': serializer.validated_data.get('cans_Trauma_Exp'),

                  'Family support': serializer.validated_data.get('family_support'),
                  'Level of aggression': serializer.validated_data.get('level_of_aggression'),
                  'Fire setting': serializer.validated_data.get('fire_setting'),
                  'Abuse, or neglect': serializer.validated_data.get('abuse_neglect'),
                  'Screening tool for Trauma--Total score': serializer.validated_data.get('Screening_tool_Trauma')
                  }  # 'AgeAtEnrollStart': serializer.validated_data.get('ageAtEnrollStart'),

            data = pd.DataFrame(dt, index=[0])

            # Impute empty values with mean values

            if data['Family support'][0] is None:
                if data['Gender'][0] == 1:
                    data['Family support'] = 1.148148
                else:
                    data['Family support'] = 0.963964
            if data['Level of aggression'][0] is None:
                if data['Gender'][0] == 2:
                    data['Level of aggression'] = 2.369863
                else:
                    data['Level of aggression'] = 2.053333
            if data['Fire setting'][0] is None:
                if data['Gender'][0] == 1:
                    data['Fire setting'] = 0.068493
                else:
                    data['Fire setting'] = 0.213333
            if data['Client self-harm'][0] is None:
                if data['Gender'][0] == 1:
                    data['Client self-harm'] = 0.479452
                else:
                    data['Client self-harm'] = 0.197309
            # if data['Abuse, or neglect'][0] is None:
            #     if data['Gender'][0] == 1:
            #         data['Abuse, or neglect'] = 0.613636
            #     else:
            #         data['Abuse, or neglect'] = 0.535398
            if data['CANS_LifeFunctioning'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_LifeFunctioning'] = 12.945205
                else:
                    data['CANS_LifeFunctioning'] = 11.475556

            if data['CANS_YouthStrengths'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_YouthStrengths'] = 13.704225
                else:
                    data['CANS_YouthStrengths'] = 13.157407
            if data['CANS_CareGiverStrengths'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_CareGiverStrengths'] = 10.129032
                else:
                    data['CANS_CareGiverStrengths'] = 7.107692
            if data['CANS_Culture'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_Culture'] = 0.05797
                else:
                    data['CANS_Culture'] = 0.148718
            if data['CANS_YouthBehavior'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_YouthBehavior'] = 9.438356
                else:
                    data['CANS_YouthBehavior'] = 7.733333
            if data['CANS_YouthRisk'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_YouthRisk'] = 4.191781
                else:
                    data['CANS_YouthRisk'] = 3.986667
            if data['CANS_Trauma_Exp'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_Trauma_Exp'] = 5.042857
                else:
                    data['CANS_Trauma_Exp'] = 4.360976
            # if data['FAST_FamilyTogetherScore'][0] is None:
            #     if data['Gender'][0] == 1:
            #         data['FAST_FamilyTogetherScore'] = 7.377358
            #     else:
            #         data['FAST_FamilyTogetherScore'] = 7.245283
            # if data['FAST_CaregiverAdvocacyScore'][0] is None:
            #     if data['Gender'][0] == 1:
            #         data['FAST_CaregiverAdvocacyScore'] = 6.674419
            #     else:
            #         data['FAST_CaregiverAdvocacyScore'] = 5.887500
            if data['YLS_PriorCurrentOffenses_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_PriorCurrentOffenses_Score'] = 0.684211
                else:
                    data['YLS_PriorCurrentOffenses_Score'] = 0.566667
            if data['YLS_FamCircumstances_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_FamCircumstances_Score'] = 3.750000
                else:
                    data['YLS_FamCircumstances_Score'] = 2.811111
            if data['YLS_Edu_Employ_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Edu_Employ_Score'] = 2.944444
                else:
                    data['YLS_Edu_Employ_Score'] = 2.322222
            if data['YLS_Peer_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Peer_Score'] = 2.833333
                else:
                    data['YLS_Peer_Score'] = 1.944444
            if data['YLS_Subab_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Subab_Score'] = 2.166667
                else:
                    data['YLS_Subab_Score'] = 1.311111
            if data['YLS_Leisure_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Leisure_Score'] = 1.944444
                else:
                    data['YLS_Leisure_Score'] = 2.000000
            if data['YLS_Personality_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Personality_Score'] = 3.555556
                else:
                    data['YLS_Personality_Score'] = 3.188889
            if data['YLS_Attitude_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Attitude_Score'] = 1.944444
                else:
                    data['YLS_Attitude_Score'] = 1.377778
            if data['Screening tool for Trauma--Total score'][0] is None:
                if data['Gender'][0] == 1:
                    data['Screening tool for Trauma--Total score'] = 14.595238
                else:
                    data['Screening tool for Trauma--Total score'] = 14.634409

            # data = data.fillna(0) #,axis = 1,inplace=True

            Feature_names = ['EpisodeNumber', 'Number of foster care placements', 'AgeAtEpisodeStart',
                             'Number of prior placements \n(excluding shelter and detention)',
                             'Number of prior treatment terminations (excluding shelter or detention)',
                             'Length of time since living at home', 'Termination directly to AV',
                             'Death Caregiver', 'Borderline IQ (below 70)', 'Hist of prior program SAO',
                             'Death Silblings', 'Alcohol Use', 'Drug Use', 'Incarcerated caregivers',
                             'Incarcerated siblings', 'Number of prior AWOLS', 'Animal cruelty',
                             'Number of prior hospitalizations', 'Compliant with medication',
                             'Significant mental health symptoms', 'Severe mental health symptoms',
                             'Autism Diagnosis', 'Borderline Personality', 'Psychosis',
                             'Reactive Attachment Disorder', 'Schizophrenia', 'YLS_PriorCurrentOffenses_Score',
                             'YLS_FamCircumstances_Score',
                             'YLS_Edu_Employ_Score', 'YLS_Peer_Score', 'YLS_Subab_Score',
                             'YLS_Leisure_Score', 'YLS_Personality_Score', 'YLS_Attitude_Score', 'Client self-harm',
                             'CANS_LifeFunctioning',
                             'CANS_YouthStrengths', 'CANS_CareGiverStrengths', 'CANS_Culture',
                             'CANS_YouthBehavior', 'CANS_YouthRisk', 'CANS_Trauma_Exp', 'Family support',
                             'Level of aggression', 'Fire setting',
                             'Abuse, or neglect', 'Screening tool for Trauma--Total score']  # 'AgeAtEnrollStart',

            # 11/12/2019
            numeric_cols = ['Gender', 'PrimaryRacecode', 'LS_Type', 'CYF_code', 'RefSourceName', 'EpisodeNumber',
                            'Number of foster care placements', 'AgeAtEpisodeStart',

                            'Number of prior placements \n(excluding shelter and detention)', 'AgeAtEnrollStart',

                            'Number of prior treatment terminations (excluding shelter or detention)',

                            'Length of time since living at home', 'Termination directly to AV',

                            'Death Caregiver', 'Borderline IQ (below 70)', 'Hist of prior program SAO',

                            'Death Silblings', 'Alcohol Use', 'Drug Use', 'Incarcerated caregivers',

                            'Incarcerated siblings', 'Number of prior AWOLS', 'Animal cruelty',

                            'Number of prior hospitalizations', 'Compliant with medication',

                            'Significant mental health symptoms', 'Severe mental health symptoms',

                            'Autism Diagnosis', 'Borderline Personality', 'Psychosis',

                            'Reactive Attachment Disorder',
                            'Schizophrenia']  # 'Program',, 'Level_of_Care', 'FacilityType'

            dummies = pd.DataFrame()
            # converting float to integer
            for col in numeric_cols:
                data[col] = pd.to_numeric(data[col], errors='coerce', downcast='integer')

            data['PrimaryRacecode'].fillna(data['PrimaryRacecode'].mode()[0], inplace=True)
            data['PrimaryRacecode'] = data['PrimaryRacecode'].astype('int')

            for column in ['Gender', 'PrimaryRacecode', 'LS_Type', 'CYF_code', 'RefSourceName']:
                dummies1 = pd.get_dummies(data[column], prefix=column)
                dummies[dummies1.columns] = dummies1.copy(deep=False)

            cols = ['Gender_1', 'Gender_2', 'PrimaryRacecode_1', 'PrimaryRacecode_2',
                    'PrimaryRacecode_3', 'PrimaryRacecode_4', 'LS_Type_1', 'LS_Type_2', 'LS_Type_3', 'LS_Type_4',
                    'LS_Type_5',
                    'CYF_code_1', 'CYF_code_2', 'RefSourceName_1', 'RefSourceName_2', 'RefSourceName_3',
                    'RefSourceName_4', 'RefSourceName_5', 'RefSourceName_6', 'RefSourceName_7', 'RefSourceName_8',
                    'RefSourceName_9', 'RefSourceName_10',
                    'RefSourceName_11', 'RefSourceName_12', 'RefSourceName_13', 'RefSourceName_14', 'RefSourceName_15',
                    'RefSourceName_16', 'RefSourceName_17', 'RefSourceName_18', 'RefSourceName_19', 'RefSourceName_20',
                    'RefSourceName_21', 'RefSourceName_22', 'RefSourceName_23', 'RefSourceName_24', 'RefSourceName_25',
                    'RefSourceName_26', 'RefSourceName_27', 'RefSourceName_28', 'RefSourceName_29', 'RefSourceName_30',
                    'RefSourceName_31', 'RefSourceName_32', 'RefSourceName_34', 'RefSourceName_35',
                    'RefSourceName_36', 'RefSourceName_37', 'RefSourceName_38',
                    'RefSourceName_39', 'RefSourceName_40', 'RefSourceName_41', 'RefSourceName_42',
                    'RefSourceName_43', 'RefSourceName_44', 'RefSourceName_45', 'RefSourceName_46', 'RefSourceName_47',
                    'RefSourceName_48', 'RefSourceName_49', 'RefSourceName_50', 'RefSourceName_51', 'RefSourceName_52',
                    'RefSourceName_53', 'RefSourceName_54', 'RefSourceName_55', 'RefSourceName_56', 'RefSourceName_57',
                    'RefSourceName_59', 'RefSourceName_60']

            for col in cols:
                if col in dummies.columns:
                    print('present', col)
                else:
                    dummies[col] = 0

            Xtest = data[Feature_names]
            Xtest[dummies.columns] = dummies
            # print("Xtest shape",Xtest.shape)
            # print("xtest columns", Xtest.columns)

            level_model = pickle.load(open("/home/ubuntu/Adelphoi/adelphoi-django/sources/LR_LC_23Dec.sav",
                                           "rb"))  # final_dt_48p_263r_2clases_smote.sav #dt_LR_Level_0.1
            program_model = pickle.load(
                open("/home/ubuntu/Adelphoi/adelphoi-django/sources/DT_P_23Dec.sav", "rb"))  # dt_T_Program
            facility_model = pickle.load(
                open("/home/ubuntu/Adelphoi/adelphoi-django/sources/LR_FT_23Dec.sav", "rb"))  # DT_FT_10Dec

            level_pred = level_model.predict(Xtest)
            program_pred = program_model.predict(Xtest)
            facility_preds = facility_model.predict(Xtest)

            program_proba = program_model.predict_proba(Xtest)

            Program_suggested = np.argmax(program_proba[0]) + 1
            Confidence = program_proba[0][Program_suggested - 1]

            print("level", level_pred)
            print("facility_preds", facility_preds)

            print(f"suggested program{Program_suggested}, with Confidence {Confidence}")

            query = Adelphoi_Mapping.objects.filter(program=program_pred,
                                                    gender=serializer.validated_data.get('gender'),
                                                    level_of_care=level_pred, facility_type=facility_preds)

            query2 = Adelphoi_Mapping.objects.filter(program=program_pred,
                                                     gender=serializer.validated_data.get('gender'),
                                                     level_of_care=level_pred)
            for qq in query2:
                print(qq)
            serializer.save(program=program_pred, level_of_care=level_pred, facility_type=facility_preds,
                            confidence=Confidence,
                            family_support=data['Family support'][0],
                            level_of_aggression=data['Level of aggression'][0],
                            fire_setting=data['Fire setting'][0],
                            client_self_harm=data['Client self-harm'][0],
                            cans_LifeFunctioning=data['CANS_LifeFunctioning'][0],
                            cans_YouthStrengths=data['CANS_YouthStrengths'][0],
                            cans_CareGiverStrengths=data['CANS_CareGiverStrengths'][0],
                            cans_Culture=data['CANS_Culture'][0],
                            cans_YouthBehavior=data['CANS_YouthBehavior'][0],
                            cans_YouthRisk=data['CANS_YouthRisk'][0],
                            cans_Trauma_Exp=data['CANS_Trauma_Exp'][0],
                            yls_PriorCurrentOffenses_Score=data['YLS_PriorCurrentOffenses_Score'][0],
                            yls_FamCircumstances_Score=data['YLS_FamCircumstances_Score'][0],
                            yls_Edu_Employ_Score=data['YLS_Edu_Employ_Score'][0],
                            yls_Peer_Score=data['YLS_Peer_Score'][0],
                            yls_Subab_Score=data['YLS_Subab_Score'][0],
                            yls_Leisure_Score=data['YLS_Leisure_Score'][0],
                            yls_Personality_Score=data['YLS_Personality_Score'][0],
                            yls_Attitude_Score=data['YLS_Attitude_Score'][0],
                            Screening_tool_Trauma=data['Screening tool for Trauma--Total score'][
                                0])  # family_support = data['Family support'],
            # FAST_FamilyTogetherScore = data['FAST_FamilyTogetherScore'][0],
            # FAST_CaregiverAdvocacyScore = data['FAST_CaregiverAdvocacyScore'][0],
            #######
            location_list = []
            program_list = []
            level_list = []
            facility_names = []
            program_model = []
            if query.count() > 0:
                for i in query:
                    program_list.append(i.program_name)
                    level_list.append(i.level_names)
                    location_list.append(i.location_names)
                    facility_names.append(i.facility_names)
                    program_model.append(i.program_model_suggested)
                return Response(
                    {"program": program_pred, "program list is": program_list, "level of care is ": level_list,
                     "location names": location_list, "facility names": facility_names, "Confidence": Confidence,
                     "program_model_suggested": program_model})
            elif query2.count() > 0:
                for i in query:
                    program_list.append(i.program_name)
                    level_list.append(i.level_names)
                    location_list.append(i.location_names)
                    facility_names.append(i.facility_names)
                    program_model.append(i.program_model_suggested)
                return Response(
                    {"program": program_pred, "program list is": program_list, "level of care is ": level_list,
                     "location names": location_list, "facility names": facility_names, "Confidence": Confidence,
                     "program_model_suggested": program_model})

            else:
                return Response({"program": program_pred, "Level of care": level_pred, "Confidence": Confidence,
                                 "Facility Type": facility_preds, "ERROR": "Matching values not found"})
        else:
            serializer.save()
            return Response({"data": "Thanx"})

        return Response({"data": "Failure"})


class AdelphoiSubmission(RetrieveUpdateAPIView):  # UpdateAPIView

    serializer_class = ProgramLevelSerialzer  # ModelTestsSerializers_selected_program, ModelTestsSerializer_program_model_suggested
    # serializer_class = ModelTestsSerializer_program_model_suggested
    queryset = ModelTests.objects.all()

    def put(self, request, *args, **kwargs):
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        print(mt.program)
        print(mt.gender)
        suggested_programs2 = request.GET['suggested_programs']
        location = request.GET['location_names']

        query = Adelphoi_Mapping.objects.filter(
            gender=mt.gender)  # ,program_model_suggested = serializer.validated_data.get("program_model_suggested")
        suggested_programs = []
        suggested_location = []
        location_names = []

        selected_program = []
        selected_level = []
        selected_facility = []
        if query.count() > 0:
            for i in query:
                suggested_programs.append(i.program_model_suggested)
                suggested_location.append(i.location_names)
            query_location = Adelphoi_Mapping.objects.filter(program_model_suggested=suggested_programs2)
            for q in query_location:
                location_names.append(q.location_names)
                selected_program.append(q.program)
                selected_level.append(q.level_of_care)
                selected_facility.append(q.facility_type)
        data = {"suggested_programs": suggested_programs, "location_names": suggested_location}

        mt.client_selected_level = int(selected_level[0])
        mt.client_selected_facility = int(selected_facility[0])
        mt.client_selected_program = int(selected_program[0])
        mt.save()

        return Response({"data": data})

    def get(self, request, *args, **kwargs):
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        print(mt.program)
        query = Adelphoi_Mapping.objects.filter(gender=mt.gender)
        suggested_programs = []
        locatin_name = []
        for i in query:
            suggested_programs.append(i.program_model_suggested)
            locatin_name.append(i.location_names)
        data = {"suggested_programs": suggested_programs}
        return Response(data)


class Adelphoi_program(ListAPIView):
    def get(self, request, *args, **kwargs):
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        print(mt.program)
        print(mt.gender)

        query = Adelphoi_Mapping.objects.filter(
            gender=mt.gender)  # ,program_model_suggested = serializer.validated_data.get("program_model_suggested")
        suggested_programs = []
        for i in query:
            suggested_programs.append(i.program_model_suggested)
        data = {
            'program_model_suggested': suggested_programs,
        }
        return Response(data)


class Adelphoi_location(ListAPIView):
    def get(self, request, *args, **kwargs):
        client_selected_program = request.GET['client_selected_program']
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        query = Adelphoi_Mapping.objects.filter(program_model_suggested=client_selected_program,
                                                gender=mt.gender)  # ,program_model_suggested = serializer.validated_data.get("program_model_suggested")
        suggested_location = []
        if query.count() > 0:
            for i in query:
                suggested_location.append(i.location_names)
        else:
            return Response({"result": "NO MATCHES FOUND"})
        data = {
            'Suggested Locations': suggested_location,
        }
        return Response(data)


class AdelphoiResult(UpdateAPIView):  # UpdateAPIView

    serializer_class = ProgramLocationSerialzer
    queryset = ModelTests.objects.all()

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        client_selected_program = serializer.validated_data.get(
            'client_selected_program')  # request.GET['client_selected_program']
        client_selected_location = serializer.validated_data.get(
            'client_selected_locations')  # request.GET['client_selected_location']

        query = Adelphoi_Mapping.objects.filter(gender=mt.gender)
        location_names = []

        selected_program = []
        selected_level = []
        selected_facility = []
        if query.count() > 0:
            query_location = Adelphoi_Mapping.objects.filter(program_model_suggested=client_selected_program)
            for q in query_location:
                location_names.append(q.location_names)
                selected_program.append(q.program)
                selected_level.append(q.level_of_care)
                selected_facility.append(q.facility_type)
        else:
            return Response({"Response": "not found"})

        mt.client_selected_level = int(selected_level[0])
        mt.client_selected_facility = int(selected_facility[0])
        mt.client_selected_program = int(selected_program[0])
        mt.client_selected_locations = location_names
        mt.save()
        return Response({"result": "values are inserted"})


class ProgramCompletionLevel(UpdateAPIView):
    serializer_class = ProgramLevelSerialzer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        query = ModelTests.objects.filter(client_code=kwargs['pk'])
        mt.Program_Completion = serializer.validated_data.get('Program_Completion')
        mt.Returned_to_Care = serializer.validated_data.get('Returned_to_Care')
        mt.save()
        # else:
        #     return Response({"result":"Client no exists"})
        return Response({"data": "success"})


class ClientList(ListAPIView):
    queryset = ModelTests.objects.all()
    serializer_class = FilterSerialzer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client_code', 'name']