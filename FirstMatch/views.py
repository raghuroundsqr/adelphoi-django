# Create your views here.
import json
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView

from .models import ModelTests,Adelphoi_Mapping#,Mapping_Collection  #,ModelTestSub,,Ade_Mapping
from django.views.decorators.csrf import csrf_exempt
# from .forms import TestForms,TestForms2,ModelTestForms
# from django.views import View
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
import pandas as pd
import numpy as np
import pickle
from rest_framework.parsers import JSONParser
###

from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from .serializers import ModelTestsSerializers,LocationSerializer,ModelTestsSerializers_selected_program,TestSerializer,Test2Serializer,\
    ModelTestsSerializer_program_model_suggested, ProgramSerialzer,LocationSerialzer,ProgramLocationSerialzer,ProgramLevelSerialzer,\
    AdminInterface,FilterSerialzer,UpdateSerializers,Adelphoi_placementSerializer,Adelphoi_locationSerializer
from rest_framework.parsers import JSONParser
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend



class AdelphoiList(ListCreateAPIView):
    serializer_class = ModelTestsSerializers
    # serializer_class =  ModelTestsSerializers_selected_program
    queryset = ModelTests.objects.all()
    def get(self,request):
        return Response("Success")

    # def create(self, validated_data):
    #     answer, created = ModelTests.objects.update_or_create(
    #         client_code=validated_data.get('client_code', None),
    #         defaults={'answer': validated_data.get('answer', None)})
    #     return answer
    def post(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True) #raise_exception=True

        if serializer.validated_data.get('Exclusionary_Criteria') == False:
            dt = {'Gender': serializer.validated_data.get('gender'),'PrimaryRacecode': serializer.validated_data.get('primaryRaceCode'),'AgeAtEnrollStart': serializer.validated_data.get('ageAtEnrollStart'),
                  'CYF_code': serializer.validated_data.get('CYF_code'),'LS_Type': serializer.validated_data.get('ls_type'),
                  'EpisodeNumber': serializer.validated_data.get('episode_number'),
                  'RefSourceName': serializer.validated_data.get('RefSourceCode'), 'Number of foster care placements': serializer.validated_data.get('number_of_foster_care_placements'),
                  'AgeAtEpisodeStart': serializer.validated_data.get('ageAtEpisodeStart'),'Number of prior placements \n(excluding shelter and detention)': serializer.validated_data.get('number_of_prior_placements'),
                  'Number of prior treatment terminations (excluding shelter or detention)': serializer.validated_data.get('number_of_prior_treatment_terminations'),
                  'Length of time since living at home': serializer.validated_data.get('length_of_time_since_living_at_home'),
                  'Termination directly to AV': serializer.validated_data.get('termination_directly_to_AV'),
                  'Death Caregiver': serializer.validated_data.get('death_Caregiver'), 'Borderline IQ (below 70)': serializer.validated_data.get('borderline_IQ'),
                  'Hist of prior program SAO': serializer.validated_data.get('hist_of_prior_program_SAO'),
                  'Death Silblings': serializer.validated_data.get('death_Silblings'), 'Alcohol Use': serializer.validated_data.get('alcohol_Use'), 'Drug Use': serializer.validated_data.get('drug_Use'),
                  'Incarcerated caregivers': serializer.validated_data.get('incarcerated_caregivers'),
                  'Incarcerated siblings': serializer.validated_data.get('incarcerated_siblings'), 'Number of prior AWOLS': serializer.validated_data.get('number_of_prior_AWOLS'),
                  'Animal cruelty': serializer.validated_data.get('animal_cruelty'),'Number of prior hospitalizations': serializer.validated_data.get('prior_hospitalizations'),
                  'Compliant with medication': serializer.validated_data.get('compliant_with_meds'),'Significant mental health symptoms': serializer.validated_data.get('significant_mental_health_symptoms'),
                  'Severe mental health symptoms': serializer.validated_data.get('severe_mental_health_symptoms'),
                  'Autism Diagnosis': serializer.validated_data.get('autism_Diagnosis'), 'Borderline Personality': serializer.validated_data.get('borderline_Personality'),
                  'Psychosis': serializer.validated_data.get('psychosis'),
                  'Reactive Attachment Disorder': serializer.validated_data.get('reactive_Attachment_Disorder'), 'Schizophrenia': serializer.validated_data.get('schizophrenia'),
                  'YLS_PriorCurrentOffenses_Score': serializer.validated_data.get('yls_PriorCurrentOffenses_Score'),
                  'YLS_FamCircumstances_Score': serializer.validated_data.get('yls_FamCircumstances_Score'),
                  'YLS_Edu_Employ_Score': serializer.validated_data.get('yls_Edu_Employ_Score'), 'YLS_Peer_Score': serializer.validated_data.get('yls_Peer_Score'),
                  'YLS_Subab_Score': serializer.validated_data.get('yls_Subab_Score'),'YLS_Leisure_Score': serializer.validated_data.get('yls_Leisure_Score'), 'YLS_Personality_Score': serializer.validated_data.get('yls_Personality_Score'),
                  'YLS_Attitude_Score': serializer.validated_data.get('yls_Attitude_Score'), 'Client self-harm': serializer.validated_data.get('client_self_harm'),

                  'CANS_LifeFunctioning': serializer.validated_data.get('cans_LifeFunctioning'),
                  'CANS_YouthStrengths': serializer.validated_data.get('cans_YouthStrengths'), 'CANS_CareGiverStrengths': serializer.validated_data.get('cans_CareGiverStrengths'),
                  'CANS_Culture': serializer.validated_data.get('cans_Culture'),
                  'CANS_YouthBehavior': serializer.validated_data.get('cans_YouthBehavior'), 'CANS_YouthRisk': serializer.validated_data.get('cans_YouthRisk'),
                  'CANS_Trauma_Exp': serializer.validated_data.get('cans_Trauma_Exp'),

                  'Family support': serializer.validated_data.get('family_support'), 'Level of aggression': serializer.validated_data.get('level_of_aggression'),
                  'Fire setting': serializer.validated_data.get('fire_setting'),
                  'Abuse, or neglect': serializer.validated_data.get('abuse_neglect'), 'Screening tool for Trauma--Total score': serializer.validated_data.get('Screening_tool_Trauma'),
                  'FAST_FamilyTogetherScore':serializer.validated_data.get('FAST_FamilyTogetherScore'),'FAST_CaregiverAdvocacyScore':serializer.validated_data.get('FAST_CaregiverAdvocacyScore')} #


            data = pd.DataFrame(dt, index=[0])

            # Impute empty values with mean values

            if data['Family support'][0] is None:
                if data['Gender'][0] == 1:
                    data['Family support'] = 1.152941#1.148148
                else:
                    data['Family support'] = 0.969027#0.963964
            if data['Level of aggression'][0] is None:
                if data['Gender'][0] == 1: #
                    data['Level of aggression'] = 2.3636#2.369863
                else:
                    data['Level of aggression'] = 2.052402#2.053333
            if data['Fire setting'][0] is None:
                if data['Gender'][0] == 1:
                    data['Fire setting'] = 0.0649#0.068493
                else:
                    data['Fire setting'] = 0.2096#0.213333
            if data['Client self-harm'][0] is None:
                if data['Gender'][0] == 1:
                    data['Client self-harm'] = 0.4675#0.479452
                else:
                    data['Client self-harm'] = 0.2026#0.197309
            # if data['Abuse, or neglect'][0] is None:
            #     if data['Gender'][0] == 1:
            #         data['Abuse, or neglect'] = 0.613636
            #     else:
            #         data['Abuse, or neglect'] = 0.535398
            if data['CANS_LifeFunctioning'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_LifeFunctioning'] = 13.1038#12.945205
                else:
                    data['CANS_LifeFunctioning'] = 11.4759#11.475556

            if data['CANS_YouthStrengths'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_YouthStrengths'] = 13.6800#13.704225
                else:
                    data['CANS_YouthStrengths'] = 13.1454#13.157407
            if data['CANS_CareGiverStrengths'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_CareGiverStrengths'] = 10.0757#10.129032
                else:
                    data['CANS_CareGiverStrengths'] = 7.0603#7.107692
            if data['CANS_Culture'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_Culture'] = 0.0547#0.05797
                else:
                    data['CANS_Culture'] = 0.1457#0.148718
            if data['CANS_YouthBehavior'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_YouthBehavior'] = 9.4285#9.438356
                else:
                    data['CANS_YouthBehavior'] = 7.6986#7.733333
            if data['CANS_YouthRisk'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_YouthRisk'] = 4.1038#4.191781
                else:
                    data['CANS_YouthRisk'] = 3.9912#3.986667
            if data['CANS_Trauma_Exp'][0] is None:
                if data['Gender'][0] == 1:
                    data['CANS_Trauma_Exp'] = 5.0410#5.042857
                else:
                    data['CANS_Trauma_Exp'] = 4.3349#4.360976
            if data['FAST_FamilyTogetherScore'][0] is None:
                if data['Gender'][0] == 1:
                    data['FAST_FamilyTogetherScore'] = 7.5614#7.377358
                else:
                    data['FAST_FamilyTogetherScore'] = 7.3027#7.245283
            if data['FAST_CaregiverAdvocacyScore'][0] is None:
                if data['Gender'][0] == 1:
                    data['FAST_CaregiverAdvocacyScore'] = 6.5319#6.674419
                else:
                    data['FAST_CaregiverAdvocacyScore'] = 6.0120#5.887500
            if data['YLS_PriorCurrentOffenses_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_PriorCurrentOffenses_Score'] = 0.6750#0.684211
                else:
                    data['YLS_PriorCurrentOffenses_Score'] = 0.5913#0.566667
            if data['YLS_FamCircumstances_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_FamCircumstances_Score'] = 3.7631#3.750000
                else:
                    data['YLS_FamCircumstances_Score'] = 2.7956#2.811111
            if data['YLS_Edu_Employ_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Edu_Employ_Score'] = 3.0789#2.944444
                else:
                    data['YLS_Edu_Employ_Score'] = 2.3655#2.322222
            if data['YLS_Peer_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Peer_Score'] = 2.8947#2.833333
                else:
                    data['YLS_Peer_Score'] = 1.9462#1.944444
            if data['YLS_Subab_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Subab_Score'] = 2.1578#2.166667
                else:
                    data['YLS_Subab_Score'] = 1.301#1.311111
            if data['YLS_Leisure_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Leisure_Score'] = 1.943#1.944444
                else:
                    data['YLS_Leisure_Score'] = 2.00#2.000000
            if data['YLS_Personality_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Personality_Score'] = 3.5789#3.555556
                else:
                    data['YLS_Personality_Score'] = 3.1935#3.188889
            if data['YLS_Attitude_Score'][0] is None:
                if data['Gender'][0] == 1:
                    data['YLS_Attitude_Score'] = 1.8947#1.944444
                else:
                    data['YLS_Attitude_Score'] = 1.3978#1.377778
            if data['Screening tool for Trauma--Total score'][0] is None:
                if data['Gender'][0] == 1:
                    data['Screening tool for Trauma--Total score'] = 14.7555#14.595238
                else:
                    data['Screening tool for Trauma--Total score'] = 14.7244#14.634409

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
                             'Abuse, or neglect', 'Screening tool for Trauma--Total score']
            #'AgeAtEnrollStart',
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

                            'Reactive Attachment Disorder', 'Schizophrenia'] #'Program',, 'Level_of_Care', 'FacilityType'

            dummies = pd.DataFrame()
            #converting float to integer
            for col in numeric_cols:
                data[col] = pd.to_numeric(data[col], errors='coerce', downcast='integer')

            data['PrimaryRacecode'].fillna(data['PrimaryRacecode'].mode()[0],inplace = True)
            data['PrimaryRacecode'] = data['PrimaryRacecode'].astype('int')

            for column in ['Gender', 'PrimaryRacecode', 'LS_Type', 'CYF_code', 'RefSourceName']:
                dummies1 = pd.get_dummies(data[column], prefix=column)
                dummies[dummies1.columns] = dummies1.copy(deep=False)

            cols = ['Gender_1', 'Gender_2', 'PrimaryRacecode_1', 'PrimaryRacecode_2',
                    'PrimaryRacecode_3','PrimaryRacecode_4','LS_Type_1', 'LS_Type_2','LS_Type_3','LS_Type_4', 'LS_Type_5',
                    'CYF_code_1', 'CYF_code_2', 'RefSourceName_1','RefSourceName_2', 'RefSourceName_3',
                    'RefSourceName_4', 'RefSourceName_5', 'RefSourceName_6','RefSourceName_7', 'RefSourceName_8', 'RefSourceName_9','RefSourceName_10',
                    'RefSourceName_11','RefSourceName_12','RefSourceName_13', 'RefSourceName_14', 'RefSourceName_15',
                    'RefSourceName_16', 'RefSourceName_17', 'RefSourceName_18','RefSourceName_19','RefSourceName_20',
                    'RefSourceName_21','RefSourceName_22','RefSourceName_23','RefSourceName_24', 'RefSourceName_25',
                    'RefSourceName_26', 'RefSourceName_27','RefSourceName_28','RefSourceName_29','RefSourceName_30',
                    'RefSourceName_31','RefSourceName_32','RefSourceName_34', 'RefSourceName_35',
                    'RefSourceName_36', 'RefSourceName_37', 'RefSourceName_38',
                    'RefSourceName_39','RefSourceName_40', 'RefSourceName_41', 'RefSourceName_42',
                    'RefSourceName_43', 'RefSourceName_44','RefSourceName_45','RefSourceName_46','RefSourceName_47',
                    'RefSourceName_48','RefSourceName_49','RefSourceName_50','RefSourceName_51', 'RefSourceName_52',
                    'RefSourceName_53','RefSourceName_54','RefSourceName_55','RefSourceName_56','RefSourceName_57',
                    'RefSourceName_59','RefSourceName_60']

            for col in cols:
                if col in dummies.columns:
                    print('present', col)
                else:
                    dummies[col] = 0

            Xtest = data[Feature_names]
            Xtest[dummies.columns] = dummies


            level_model = pickle.load(open("C:/Users/Raghu/Downloads/LR_LC_23Dec.sav", "rb")) #/home/ubuntu/Adelphoi/adelphoi-django/sources/LR_LC_23Dec.sav   # final_dt_48p_263r_2clases_smote.sav #dt_LR_Level_0.1
            program_model = pickle.load(open("C:/Users/Raghu/Downloads/DT_P_23Dec.sav", "rb")) #/home/ubuntu/Adelphoi/adelphoi-django/sources/DT_P_23Dec.sav #dt_T_Program
            facility_model= pickle.load(open("C:/Users/Raghu/Downloads/LR_FT_23Dec.sav", "rb")) # /home/ubuntu/Adelphoi/adelphoi-django/sources/LR_FT_23Dec.sav#DT_FT_10Dec

            level_pred = level_model.predict(Xtest)
            program_pred = program_model.predict(Xtest)
            facility_preds = facility_model.predict(Xtest)

            program_proba = program_model.predict_proba(Xtest)
            level_proba = level_model.predict_proba(Xtest)
            facility_proba = facility_model.predict_proba(Xtest)

            Program_suggested = np.argmax(program_proba[0]) + 1
            Confidence = program_proba[0][Program_suggested - 1]

            level_proba1 = np.argmax(level_proba[0]) + 1
            Confidence1 = level_proba[0][level_proba1 - 1]

            facility_proba1 = np.argmax(facility_proba[0])+1
            Confidence2 = facility_proba[0][facility_proba1 - 1]

            # print("Confidence",Confidence)
            # print("Confidence1",Confidence1)
            #
            # print("level",level_pred)
            # print("facility_preds",facility_preds)
            #
            # print(f"suggested program{Program_suggested}, with Confidence {Confidence}")
            # print(f"level of care {level_proba1},with confidence {Confidence1}")
            #
            # print("program_pred",program_pred)

            query = Adelphoi_Mapping.objects.filter(program=program_pred, gender=serializer.validated_data.get('gender'), level_of_care=level_pred,facility_type = facility_preds)

            serializer.save(program=program_pred,level_of_care=level_pred,facility_type =facility_preds,confidence = Confidence,
                            family_support = data['Family support'][0],
                            level_of_aggression = data['Level of aggression'][0],
                            fire_setting = data['Fire setting'][0],
                            client_self_harm = data['Client self-harm'][0],
                            cans_LifeFunctioning = data['CANS_LifeFunctioning'][0],
                            cans_YouthStrengths = data['CANS_YouthStrengths'][0],
                            cans_CareGiverStrengths = data['CANS_CareGiverStrengths'][0],
                            cans_Culture = data['CANS_Culture'][0],
                            cans_YouthBehavior = data['CANS_YouthBehavior'][0],
                            cans_YouthRisk = data['CANS_YouthRisk'][0],
                            cans_Trauma_Exp = data['CANS_Trauma_Exp'][0],
                            yls_PriorCurrentOffenses_Score = data['YLS_PriorCurrentOffenses_Score'][0],
                            yls_FamCircumstances_Score = data['YLS_FamCircumstances_Score'][0],
                            yls_Edu_Employ_Score  = data['YLS_Edu_Employ_Score'][0],
                            yls_Peer_Score = data['YLS_Peer_Score'][0],
                            yls_Subab_Score = data['YLS_Subab_Score'][0],
                            yls_Leisure_Score = data['YLS_Leisure_Score'][0],
                            yls_Personality_Score = data['YLS_Personality_Score'][0],
                            yls_Attitude_Score = data['YLS_Attitude_Score'][0],
                            Screening_tool_Trauma = data['Screening tool for Trauma--Total score'][0],
                            FAST_FamilyTogetherScore=data['FAST_FamilyTogetherScore'][0],
                            FAST_CaregiverAdvocacyScore = data['FAST_CaregiverAdvocacyScore'][0]
                            ) #family_support = data['Family support'],
                            # FAST_FamilyTogetherScore = data['FAST_FamilyTogetherScore'][0],
                            # FAST_CaregiverAdvocacyScore = data['FAST_CaregiverAdvocacyScore'][0],
            #######
            location_list = []
            program_list = []
            level_list = []
            facility_names = []
            program_model = []
            program_type = []
            if query.count()>0:
                if serializer.validated_data.get('gender') == 1:
                    condition_program = 3
                    serializer.save(condition_program = condition_program)
                    for i in query:
                        program_list.append(i.program_name)
                        level_list.append(i.level_names)
                        facility_names.append(i.facility_names)
                        program_type.append(i.program_type)

                    return Response(
                        {"model program": program_pred,"program": condition_program, "Level of care": level_pred,
                         "program_type": program_type,
                         "Facility Type": facility_preds,
                         "program Confidence": Confidence, "facility Confidence": Confidence2,
                         "level Confidence": Confidence1, "gender": serializer.validated_data.get('gender')})
                else:
                    for i in query:
                        program_list.append(i.program_name)
                        level_list.append(i.level_names)
                        facility_names.append(i.facility_names)
                        program_type.append(i.program_type)
                    return Response({"program": program_pred, "Level of care": level_pred, "program_type": program_type,
                                 "Facility Type": facility_preds,
                                 "program Confidence": Confidence, "facility Confidence": Confidence2,
                                 "level Confidence": Confidence1, "gender": serializer.validated_data.get('gender')})
            else:
                if serializer.validated_data.get('gender') == 1:
                    condition_program = 3
                    serializer.save(condition_program=condition_program)
                    for i in query:
                        program_list.append(i.program_name)
                        level_list.append(i.level_names)
                        facility_names.append(i.facility_names)
                        program_type.append(i.program_type)
                    return Response(
                        {"model program": program_pred, "program": condition_program, "Level of care": level_pred,
                         "program_type": program_type,
                         "Facility Type": facility_preds,
                         "program Confidence": Confidence, "facility Confidence": Confidence2,
                         "level Confidence": Confidence1, "gender": serializer.validated_data.get('gender')})
                else:
                    for i in query:
                        program_list.append(i.program_name)
                        level_list.append(i.level_names)
                        facility_names.append(i.facility_names)
                        program_type.append(i.program_type)
                    return Response({"program": program_pred, "Level of care": level_pred, "program_type": program_type,
                                 "Facility Type": facility_preds,
                                 "program Confidence": Confidence, "facility Confidence": Confidence2,
                                 "level Confidence": Confidence1, "gender": serializer.validated_data.get('gender')})

                # return Response({"program": program_pred,"program_type": program_type,"Level of care":level_pred,"Confidence":Confidence,"Facility Type":facility_preds,
                #                  "program Confidence": Confidence,"facility Confidence":Confidence2,
                #                  "level Confidence":Confidence1,"gender":serializer.validated_data.get('gender'),"ERROR":"Matching values not found"})
        else:
            serializer.save()
            return Response({"Result":"Thanx for registering with ADELPHOI"})
        return Response({"data": "Failure"})

class Adelphoi_placement(RetrieveAPIView):
    serializer_class = Adelphoi_placementSerializer
    queryset = ModelTests.objects.all()

    # def get(self, request, *args, **kwargs):
    #     mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk']).first()
    #     # print(mt.referred_program)
    #     if mt:
    #         referred_program = mt.referred_program
    #         model_program = mt.model_program
    #         return Response({"Referred program":referred_program,"Model Program":model_program})
    #     else:
    #         return Response({"result":"client not exists"})

# class Adelphoi_placement(ListAPIView):
#     def get(self, request, *args, **kwargs):
#         mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
#         referred_program = mt.referred_program
#         model_program = mt.model_program
#         return Response({"Referred program":referred_program,"Model Program":model_program})
# class Adelphoi_location(RetrieveAPIView):
#     serializer_class = Adelphoi_locationSerializer
#     queryset = Adelphoi_Mapping.objects.filter(client_code=kwargs['pk'])

class Adelphoi_location(ListAPIView):
    def get(self, request, *args, **kwargs):
        client_selected_program = request.GET['client_selected_program']
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])
        if mt.exists():
            query = Adelphoi_Mapping.objects.filter(program_type = client_selected_program) #,program_model_suggested = serializer.validated_data.get("program_model_suggested")
            suggested_location = []
            if query.count()>0:
                for i in query:
                    suggested_location.append(i.location_names)
            else:
                return Response({"result":"NO MATCHES FOUND"})
            return Response({'Suggested Locations': suggested_location[0]})
        else:
            return Response({"result":"client not exists"})
        return Response({"result":"failure"})

#
# class AdelphoiResult(UpdateAPIView):  #UpdateAPIView
#
#     serializer_class = ProgramLocationSerialzer
#     queryset = ModelTests.objects.all()

class AdelphoiResult(UpdateAPIView):  #UpdateAPIView

    serializer_class = ProgramLocationSerialzer
    queryset = ModelTests.objects.all()

    def put(self,request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        client_selected_program = serializer.validated_data.get('client_selected_program') #request.GET['client_selected_program']
        client_selected_location = serializer.validated_data.get('client_selected_locations') #request.GET['client_selected_location']

        location_names = []
        selected_program = []
        selected_level = []
        selected_facility = []
        query_location = Adelphoi_Mapping.objects.filter(program_type = client_selected_program)
        if query_location.count()>0:
            for q in query_location:
                location_names.append(q.location_names)
                selected_program.append(q.program)
                selected_level.append(q.level_of_care)
                selected_facility.append(q.facility_type)
        else:
            return Response({"Response":"not found"})

        mt.client_selected_level = int(selected_level[0])
        mt.client_selected_facility = int(selected_facility[0])
        # mt.client_selected_program = int(selected_program[0])
        mt.client_selected_program = client_selected_program
        mt.client_selected_locations = client_selected_location
        mt.save()
        return Response({"result":"values are inserted"})

# class AdelphoiResult(UpdateAPIView):  #UpdateAPIView
#
#     serializer_class = ProgramLocationSerialzer
#     queryset = ModelTests.objects.all()
#
#     def put(self,request, *args, **kwargs):
#         serializer = self.get_serializer_class()
#         serializer = serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk']).first()
#         if mt:
#             client_selected_program = serializer.validated_data.get('client_selected_program') #request.GET['client_selected_program']
#             client_selected_location = serializer.validated_data.get('client_selected_locations') #request.GET['client_selected_location']
#
#             location_names = []
#             selected_program = []
#             selected_level = []
#             selected_facility = []
#
#             query_location = Adelphoi_Mapping.objects.filter(program_type = client_selected_program)
#             if query_location.count()>0:
#                 for q in query_location:
#                     location_names.append(q.location_names)
#                     selected_program.append(q.program)
#                     selected_level.append(q.level_of_care)
#                     selected_facility.append(q.facility_type)
#             else:
#                 return Response({"Response":"not found"})
#
#             mt.client_selected_level = int(selected_level[0])
#             mt.client_selected_facility = int(selected_facility[0])
#             # mt.client_selected_program = int(selected_program[0])
#             mt.client_selected_program = client_selected_program
#             mt.client_selected_locations = client_selected_location
#             mt.save()
#             return Response({"result":"values are inserted"})
#         else:
#             return Response({"result":"client not exists"})
# class AdelphoiResult(UpdateAPIView):  #UpdateAPIView
#
#     serializer_class = ProgramLocationSerialzer
#     queryset = ModelTests.objects.all()
#
#     def put(self,request, *args, **kwargs):
#         serializer = self.get_serializer_class()
#         serializer = serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
#         client_selected_program = serializer.validated_data.get('client_selected_program') #request.GET['client_selected_program']
#         client_selected_location = serializer.validated_data.get('client_selected_locations') #request.GET['client_selected_location']
#
#
#         location_names = []
#
#         selected_program = []
#         selected_level = []
#         selected_facility = []
#         query_location = Adelphoi_Mapping.objects.filter(program_type = client_selected_program)
#         if query_location.count()>0:
#             for q in query_location:
#                 location_names.append(q.location_names)
#                 selected_program.append(q.program)
#                 selected_level.append(q.level_of_care)
#                 selected_facility.append(q.facility_type)
#         else:
#             return Response({"Response":"not found"})
#
#         mt.client_selected_level = int(selected_level[0])
#         mt.client_selected_facility = int(selected_facility[0])
#         # mt.client_selected_program = int(selected_program[0])
#         mt.client_selected_program = client_selected_program
#         mt.client_selected_locations = client_selected_location
#         mt.save()
#         return Response({"result":"values are inserted"})


#Update program completion and returned to care to values after a while. Values will be  updated
class ProgramCompletionLevel(UpdateAPIView): #UpdateAPIView
    serializer_class = ProgramLevelSerialzer
    queryset = ModelTests.objects.all()

    def put(self,request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk']).first()
        if mt:
            mt.Program_Completion = serializer.validated_data.get('Program_Completion')
            mt.Returned_to_Care = serializer.validated_data.get('Returned_to_Care')
            mt.save()
            # else:
            #     return Response({"result":"Client no exists"})
            return Response({"data":"success"})
        else:
            return Response({"result":"client not exists"})
#To search results based on client_code or name
class ClientList(ListAPIView):
    queryset = ModelTests.objects.all()
    serializer_class = FilterSerialzer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client_code','name']

#to save adelphoi mapping values from admin

@csrf_exempt
def saveData(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        #
        program = data['program']
        program_name = data['program_name']
        gender = data['gender']
        gender_name = data['gender_name']
        level_of_care = data['level_of_care']
        level_names = data['level_names']

        location = data['location']
        location_names = data['location_names']

        facility_type = data['facility_type']
        facility_names = data['facility_names']
        program_model_suggested = data['program_model_suggested']
        program_type = data['program_type']

        print("location:",location)

        Adelphoi_Mapping(location = list(eval(location)),location_names = location_names.split(','),program = program,program_name = program_name,\
                         gender =gender,gender_name = gender_name,level_of_care = level_of_care,level_names =level_names,\
                         facility_type = facility_type,facility_names =facility_names,program_model_suggested = program_model_suggested,\
                         program_type = program_type).save()
        return JsonResponse({"data":"Data inserted successfully"})
    else:
        return JsonResponse({"data","Method not allowed"})

# class UpdateLogic(RetrieveUpdateDestroyAPIView):
#     queryset = ModelTests.objects.all()
#     serializer_class = ModelTestsSerializers



class UpdateLogic(RetrieveUpdateDestroyAPIView):
    queryset = ModelTests.objects.all()
    serializer_class = ModelTestsSerializers

    def put(self, request, pk,*args, **kwargs): #
        print("am here")
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # write your logic here
        # pk.borderline_Personality  = request.data['borderline_Personality']
        # print("valie",serializer.validated_data.get('borderline_Personality'))
        # pk.save()
        print("am done")
        # data = serializer.data
        # print(data)
        # print(serializer.validated_data.get('gender'))

        return Response({"data":"success"})

@csrf_exempt
def update_logic(request,pk):
    try:
        query = ModelTests.objects.get(pk=pk)
        print(query)
    except ModelTests.DoesNotExist:
        return HttpResponse(status=404)
        # return Response({"data":"one"})
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UpdateSerializers(query, data=data)
        if serializer.is_valid():
            if serializer.validated_data.get('Exclusionary_Criteria') == False:
                dt = {'Gender': serializer.validated_data.get('gender'),
                      'PrimaryRacecode': serializer.validated_data.get('primaryRaceCode'),
                      'AgeAtEnrollStart': serializer.validated_data.get('ageAtEnrollStart'),
                      'CYF_code': serializer.validated_data.get('CYF_code'),
                      'LS_Type': serializer.validated_data.get('ls_type'),
                      'EpisodeNumber': serializer.validated_data.get('episode_number'),
                      'RefSourceName': serializer.validated_data.get('RefSourceCode'),
                      'Number of foster care placements': serializer.validated_data.get(
                          'number_of_foster_care_placements'),
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
                      }  #

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
                                 'Abuse, or neglect', 'Screening tool for Trauma--Total score']
                # 'AgeAtEnrollStart',
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
                        'RefSourceName_11', 'RefSourceName_12', 'RefSourceName_13', 'RefSourceName_14',
                        'RefSourceName_15',
                        'RefSourceName_16', 'RefSourceName_17', 'RefSourceName_18', 'RefSourceName_19',
                        'RefSourceName_20',
                        'RefSourceName_21', 'RefSourceName_22', 'RefSourceName_23', 'RefSourceName_24',
                        'RefSourceName_25',
                        'RefSourceName_26', 'RefSourceName_27', 'RefSourceName_28', 'RefSourceName_29',
                        'RefSourceName_30',
                        'RefSourceName_31', 'RefSourceName_32', 'RefSourceName_34', 'RefSourceName_35',
                        'RefSourceName_36', 'RefSourceName_37', 'RefSourceName_38',
                        'RefSourceName_39', 'RefSourceName_40', 'RefSourceName_41', 'RefSourceName_42',
                        'RefSourceName_43', 'RefSourceName_44', 'RefSourceName_45', 'RefSourceName_46',
                        'RefSourceName_47',
                        'RefSourceName_48', 'RefSourceName_49', 'RefSourceName_50', 'RefSourceName_51',
                        'RefSourceName_52',
                        'RefSourceName_53', 'RefSourceName_54', 'RefSourceName_55', 'RefSourceName_56',
                        'RefSourceName_57',
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

                level_model = pickle.load(open("C:/Users/Raghu/Downloads/LR_LC_23Dec.sav",
                                               "rb"))  # /home/ubuntu/Adelphoi/adelphoi-django/sources/LR_LC_23Dec.sav   # final_dt_48p_263r_2clases_smote.sav #dt_LR_Level_0.1
                program_model = pickle.load(open("C:/Users/Raghu/Downloads/DT_P_23Dec.sav",
                                                 "rb"))  # /home/ubuntu/Adelphoi/adelphoi-django/sources/DT_P_23Dec.sav #dt_T_Program
                facility_model = pickle.load(open("C:/Users/Raghu/Downloads/LR_FT_23Dec.sav",
                                                  "rb"))  # /home/ubuntu/Adelphoi/adelphoi-django/sources/LR_FT_23Dec.sav#DT_FT_10Dec

                level_pred = level_model.predict(Xtest)
                program_pred = program_model.predict(Xtest)
                facility_preds = facility_model.predict(Xtest)

                program_proba = program_model.predict_proba(Xtest)

                Program_suggested = np.argmax(program_proba[0]) + 1
                Confidence = program_proba[0][Program_suggested - 1]

                Program_suggested1 = np.argmax(program_proba[0]) + 1
                Confidence1 = program_proba[0][Program_suggested1 - 1]
                print("Confidence", Confidence)
                print("Confidence1", Confidence1)

                print("level", level_pred)
                print("facility_preds", facility_preds)

                print(f"suggested program{Program_suggested}, with Confidence {Confidence}")

                print("program_pred", program_pred)

                query = Adelphoi_Mapping.objects.filter(program=program_pred,
                                                        gender=serializer.validated_data.get('gender'),
                                                        level_of_care=level_pred, facility_type=facility_preds)
                query2 = Adelphoi_Mapping.objects.filter(program=program_pred,
                                                         gender=serializer.validated_data.get('gender'),
                                                         level_of_care=level_pred)  # , level_of_care=level_pred

                program_result = []
                for i in query:
                    program_result.append(i.program_type)
                print("program_result", program_result[0])
                serializer.save(program=program_pred, model_program=program_result[0], level_of_care=level_pred,
                                facility_type=facility_preds, confidence=Confidence,
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
                                Screening_tool_Trauma=data['Screening tool for Trauma--Total score'][0])  # family_support = data['Family support'],
                # FAST_FamilyTogetherScore = data['FAST_FamilyTogetherScore'][0],
                # FAST_CaregiverAdvocacyScore = data['FAST_CaregiverAdvocacyScore'][0],
                #######
                location_list = []
                program_list = []
                level_list = []
                facility_names = []
                program_model = []
                program_type = []
                if query.count() > 0:
                    for i in query:
                        program_list.append(i.program_name)
                        level_list.append(i.level_names)
                        location_list.append(i.location_names)
                        facility_names.append(i.facility_names)
                        program_model.append(i.program_model_suggested)
                        program_type.append(i.program_type)

                    print("location_list", location_list[0])
                    # return Response(
                    # {"program": program_pred, "program list is": program_list, "level of care is ": level_list,
                    #  "location names": location_list, "facility names": facility_names,"Confidence":Confidence,"program_model_suggested":program_model})
                    # return Response({"program": program_type, "Confidence": Confidence,
                    #                  "gender": serializer.validated_data.get('gender')})
                    return JsonResponse({"program": program_type, "Confidence": Confidence,
                                    "gender": serializer.validated_data.get('gender')})
                elif query2.count() > 0:
                    for i in query:
                        program_list.append(i.program_name)
                        level_list.append(i.level_names)
                        location_list.append(i.location_names)
                        facility_names.append(i.facility_names)
                        program_model.append(i.program_model_suggested)
                    # return Response(
                    #     {"program": program_pred, "program list is": program_list, "level of care is ": level_list,
                    #      "location names": location_list, "facility names": facility_names, "Confidence": Confidence,
                    #      "program_model_suggested": program_model})
                    # return Response({"program": program_type, "Confidence": Confidence,
                    #                  "gender": serializer.validated_data.get('gender')})
                    return JsonResponse({"program": program_type, "Confidence": Confidence,
                                     "gender": serializer.validated_data.get('gender')})

                else:
                    # return Response({"program": program_pred,"Level of care":level_pred,"Confidence":Confidence,"Facility Type":facility_preds,"ERROR":"Matching values not found"})
                    # return Response({"program": program_type, "gender": serializer.validated_data.get('gender'),
                    #                  "ERROR": "Matching values not found"})
                    return JsonResponse({"program": program_type, "gender": serializer.validated_data.get('gender'),
                                     "ERROR": "Matching values not found"})
            else:
                serializer.save()
                return JsonResponse({"Result": "Thanx for registering with ADELPHOI"})
            # serializer.save()
            # return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        # return Response({"data": "three"})


class UpDate(UpdateAPIView):
    serializer_class = ModelTestsSerializers
    queryset = ModelTests.objects.all()
    def put(self,request, *args, **kwargs):
        # serializer = self.get_serializer_class()
        # serializer = serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        mt.program = 3
        mt.save()
        print(mt.program)

        return Response({"data":"okay"})


###############################



class Adelphoi_program(ListAPIView):
    def get(self, request, *args, **kwargs):
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        print(mt.program)

        query = Adelphoi_Mapping.objects.filter(gender=mt.gender) #,program_model_suggested = serializer.validated_data.get("program_model_suggested")
        suggested_programs = []
        for i in query:
            suggested_programs.append(i.program_model_suggested)
        data = {
            'program_model_suggested': suggested_programs,
        }
        return Response(data)
class AdelphoiSubmission(RetrieveUpdateAPIView):  #UpdateAPIView

    serializer_class = ProgramLevelSerialzer #ModelTestsSerializers_selected_program, ModelTestsSerializer_program_model_suggested
    # serializer_class = ModelTestsSerializer_program_model_suggested
    queryset = ModelTests.objects.all()
    def put(self,request, *args, **kwargs):
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        suggested_programs2 = request.GET['suggested_programs']
        location = request.GET['location_names']
        query = Adelphoi_Mapping.objects.filter(gender=mt.gender)  # ,program_model_suggested = serializer.validated_data.get("program_model_suggested")
        suggested_programs = []
        suggested_location = []
        location_names = []

        selected_program = []
        selected_level = []
        selected_facility = []
        if query.count()>0:
            for i in query:
                suggested_programs.append(i.program_model_suggested)
                suggested_location.append(i.location_names)

            query_location = Adelphoi_Mapping.objects.filter(program_model_suggested=suggested_programs2)
            for q in query_location:
                location_names.append(q.location_names)
                selected_program.append(q.program)
                selected_level.append(q.level_of_care)
                selected_facility.append(q.facility_type)
        data = {"suggested_programs":suggested_programs,"location_names":suggested_location}

        mt.client_selected_level=int(selected_level[0])
        mt.client_selected_facility = int(selected_facility[0])
        mt.client_selected_program = int(selected_program[0])
        mt.save()

        return Response({"data":data})


    def get(self,request, *args, **kwargs):
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

class AdminUpdate(ListCreateAPIView):

    serializer_class = AdminInterface
    queryset = Adelphoi_Mapping.objects.all()

    # def post(self, request):
    #     serializer = self.get_serializer_class()
    #     serializer = serializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True) #raise_exception=True
    #     serializer.save()
    #
    #     return Response({"data":"okay"})


class Location_Mapping(UpdateAPIView):
    serializer_class = LocationSerializer

    def put(self,request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        mt.client_selected_locations = serializer.validated_data.get('client_selected_locations')
        mt.save()
        return Response({"data":"success"})



class NewAPI_1(ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = ModelTests.objects.all()



class NewAPI2(RetrieveUpdateDestroyAPIView):
    serializer_class = Test2Serializer
    queryset = ModelTests.objects.all()

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mt: ModelTests = ModelTests.objects.filter(client_code=kwargs['pk'])[0]
        print(mt.Exclusionary_Criteria)
        if mt.Exclusionary_Criteria == False:
            mt.referred_program = serializer.validated_data.get('referred_program')
            mt.save()
            return Response({"data": "success"})
        else:
            return Response({"data":"failure"})

from django.http import Http404
class Final(APIView):
    # serializer_class = ModelTestsSerializers
    # queryset = ModelTests.objects.all()
    #
    # def get_object(self, pk):
    #     try:
    #         return ModelTests.objects.get(pk=pk)
    #     except ModelTests.DoesNotExist:
    #         raise Http404

    # def put(self, request, pk, format=None):
    #     product = self.get_object(pk)
    #     serializer = ModelTestsSerializers(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        articles = ModelTests.objects.all()
        serializer = ModelTestsSerializers(articles, many=True)
        return Response({"ModelTests": serializer.data})



from .models import Musician,Album
from .serializers import MusicianSerializer,AlbumSerializer


class MusicianListView(ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()


class AlbumListView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
