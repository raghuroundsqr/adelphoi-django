# Create your views here.
import json
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView

from .models import TestModels,ModelTests,Ade_Mapping,Adelphoi_Mapping#,Mapping_Collection  #,ModelTestSub
from django.views.decorators.csrf import csrf_exempt
from .forms import TestForms,TestForms2,ModelTestForms
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
from .serializers import ModelTestsSerializers
from rest_framework.parsers import JSONParser
from django.urls import reverse_lazy
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

                return JsonResponse({'Message':"Client code already exists",'data': data, 'success': 1, 'message': 'data retrieved successfully'})

        else:
            print("new Client_code")
            aa = TestModels(Client_code = Client_code,Gender = Gender,PrimaryRacecode =PrimaryRacecode,LS_Type = LS_Type,AgeAtEpisodeStart = AgeAtEpisodeStart,
                            EpisodeNumber = EpisodeNumber,CYF_code = CYF_code,AgeAtEnrollStart = AgeAtEnrollStart,RefSourceCode =RefSourceCode,
                            Incarcerated_caregivers = Incarcerated_caregivers,Incarcerated_siblings = Incarcerated_siblings,Number_of_prior_AWOLS = Number_of_prior_AWOLS,
                            Animal_cruelty = Animal_cruelty,sexually_acting_out_in_past_program = sexually_acting_out_in_past_program,
                            prior_hospitalizations = prior_hospitalizations,Termination_directly_to_AV = Termination_directly_to_AV,
                            Autism_Diagnosis = Autism_Diagnosis,Borderline_Personality = Borderline_Personality,Compliant_with_meds  = Compliant_with_meds)

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
            
            #- Insert data to AI model
            client_code = form.cleaned_data.get('client_code')
            gender = form.cleaned_data.get('gender')
            primaryRaceCode = form.cleaned_data.get('primaryRaceCode')
            ls_type = form.cleaned_data.get('ls_type')
            ageAtEpisodeStart = form.cleaned_data.get('ageAtEpisodeStart')
            episode_number = form.cleaned_data.get('episode_number')
            CYF_code = form.cleaned_data.get('CYF_code')
            ageAtEnrollStart = form.cleaned_data.get('ageAtEnrollStart')
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
            reactive_Attachment_Disorder  = form.cleaned_data.get('reactive_Attachment_Disorder')
            schizophrenia = form.cleaned_data.get('schizophrenia')
            number_of_foster_care_placements = form.cleaned_data.get('number_of_foster_care_placements')

            episode_start = form.cleaned_data.get('episode_start')
            primary_language = form.cleaned_data.get('primary_language')
            enrollStart_date = form.cleaned_data.get('enrollStart_date')
            english_second_lang = form.cleaned_data.get('english_second_lang')
            type_of_drugs  = form.cleaned_data.get('type_of_drugs')
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
                  'AgeAtEnrollStart': ageAtEnrollStart,
                  'Number of prior treatment terminations (excluding shelter or detention)': number_of_prior_treatment_terminations,
                  'Length of time since living at home': length_of_time_since_living_at_home,
                  'Termination directly to AV': termination_directly_to_AV,
                  'Death Caregiver': death_Caregiver, 'Borderline IQ (below 70)': borderline_IQ,
                  'Hist of prior program SAO': hist_of_prior_program_SAO, #hist_of_prior_program_SAO
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

                  'CANS_LifeFunctioning': cans_LifeFunctioning ,
                 'CANS_YouthStrengths':cans_YouthStrengths, 'CANS_CareGiverStrengths':cans_CareGiverStrengths, 'CANS_Culture':cans_Culture,
                 'CANS_YouthBehavior':cans_YouthBehavior, 'CANS_YouthRisk':cans_YouthRisk, 'CANS_Trauma_Exp': cans_Trauma_Exp,
                  'Family support': family_support, 'Level of aggression': level_of_aggression, 'Fire setting': fire_setting,
                  'Abuse, or neglect': abuse_neglect, 'Screening tool for Trauma--Total score': Screening_tool_Trauma




            }





            data = pd.DataFrame(dt, index=[0])
            print(data.columns)
            print(data.shape)
            print(data)

            # du = data[['Gender','PrimaryRacecode','LS_Type','CYF code','RefSourceName']]
            # print(du)
            # dd = pd.get_dummies(du,prefix_sep='_',drop_first=True)
            # print(dd)

            Feature_names = ['EpisodeNumber', 'Number of foster care placements', 'AgeAtEpisodeStart',
                             'Number of prior placements \n(excluding shelter and detention)', 'AgeAtEnrollStart',
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

            print("features::",data[Feature_names].shape)
            dummies = pd.DataFrame()
            print("dummies shape",dummies.shape)


            for column in ['Gender', 'PrimaryRacecode', 'LS_Type', 'CYF_code', 'RefSourceName']:
                dummies1 = pd.get_dummies(data[column], prefix=column)
                dummies[dummies1.columns] = dummies1.copy(deep=False)
            print("data columns head",(data[column]).head())
            print("data columns shape", (data[column]).shape)

            print("dummies1 shape",dummies1.shape)

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

            print("dummies shape",dummies.shape)
            print(("dumm",dummies.columns))
            Xtest = data[Feature_names]
            Xtest[dummies.columns] = dummies
            Xtest.shape
            print("xtest colimns",Xtest.columns)
            ### LR JOY
            # data = data.fillna(0,inplace=True)  # remove in front end
            #pre-processing
            #
            # dummies  = pd.DataFrame()
            # for column in du:
            #     dummies1 = pd.get_dummies(data[column],prefix=column)
            #     dummies[dummies1.columns] = dummies1.copy(deep=False)
            #
            # print(dummies)

            level_model = pickle.load(open("C:/Users/Raghu/Downloads/dt_LR_Level_0.1.sav", "rb")) #final_dt_48p_263r_2clases_smote.sav
            program_model = pickle.load(open("C:/Users/Raghu/Downloads/dt_T_Program.sav", "rb"))

            # results = loaded_model.predict_proba(data)
            # print("results::", results)
            level_pred = level_model.predict(Xtest)
            program_pred = program_model.predict(Xtest)
            print(level_pred)
            print("program",program_pred)

            # Program_suggested = np.argmax(results[0]) + 1
            # Confidence = results[0][Program_suggested - 1]
            query = Ade_Mapping.objects.filter(program = program_pred,gender=gender,level_of_care = level_pred)
            location_list = []
            program_list = []
            level_list = []
            for i in query:
                program_list.append(i.program_name)
                level_list.append(i.level_name)
                location_list.append(i.location_name)
            # print(f'Model is suggesting Program - {str(Program_suggested)} with confidence of {str(round(Confidence * 100, 2))}')
            # result = (f'Model is suggesting Program - {str(Program_suggested)} locations are {location_list}') #\n with confidence of {str(round(Confidence * 100, 2))}
            result = (f'Model is suggesting Program - {program_list} -------\t level of care---{level_list}------- locations are {location_list}')  # \n with confidence of {str(round(Confidence * 100, 2))}

            # result = (f'Model is suggesting Program - {str(program_pred)} \t level of care---{str(level_pred)} locations are {location_list}')  # \n with confidence of {str(round(Confidence * 100, 2))}

            p = ModelTests(client_code = client_code,gender = gender,primaryRaceCode= primaryRaceCode,ls_type = ls_type,
                           ageAtEpisodeStart = ageAtEpisodeStart,episode_number = episode_number,CYF_code = CYF_code,ageAtEnrollStart = ageAtEnrollStart,
                           RefSourceCode = RefSourceCode,termination_directly_to_AV = termination_directly_to_AV,client_self_harm = client_self_harm,yls_PriorCurrentOffenses_Score = yls_PriorCurrentOffenses_Score,
                           yls_FamCircumstances_Score = yls_FamCircumstances_Score,yls_Edu_Employ_Score = yls_Edu_Employ_Score,yls_Peer_Score = yls_Peer_Score,
                           yls_Subab_Score = yls_Subab_Score,yls_Leisure_Score =yls_Leisure_Score,yls_Personality_Score =yls_Personality_Score,yls_Attitude_Score = yls_Attitude_Score,
                           cans_LifeFunctioning = cans_LifeFunctioning,cans_YouthStrengths = cans_YouthStrengths,cans_CareGiverStrengths = cans_CareGiverStrengths,
                           cans_Culture = cans_Culture,cans_YouthBehavior  = cans_YouthBehavior,cans_YouthRisk = cans_YouthRisk,cans_Trauma_Exp = cans_Trauma_Exp,
                           incarcerated_caregivers = incarcerated_caregivers,incarcerated_siblings = incarcerated_siblings,number_of_prior_AWOLS = number_of_prior_AWOLS,
                           animal_cruelty = animal_cruelty,hist_of_prior_program_SAO = hist_of_prior_program_SAO,prior_hospitalizations = prior_hospitalizations,
                           autism_Diagnosis = autism_Diagnosis,borderline_Personality = borderline_Personality,compliant_with_meds = compliant_with_meds,severe_mental_health_symptoms = severe_mental_health_symptoms,
                           number_of_prior_treatment_terminations = number_of_prior_treatment_terminations,length_of_time_since_living_at_home = length_of_time_since_living_at_home,
                           death_Silblings = death_Silblings,death_Caregiver = death_Caregiver,alcohol_Use = alcohol_Use,drug_Use = drug_Use,borderline_IQ = borderline_IQ,
                           significant_mental_health_symptoms = significant_mental_health_symptoms,number_of_prior_placements = number_of_prior_placements,psychosis = psychosis,
                           reactive_Attachment_Disorder = reactive_Attachment_Disorder,schizophrenia = schizophrenia,number_of_foster_care_placements = number_of_foster_care_placements,


                           level_of_care = level_pred,episode_start = episode_start, primary_language = primary_language, enrollStart_date = enrollStart_date,
            english_second_lang = english_second_lang, type_of_drugs = type_of_drugs, family_support = family_support, FAST_FamilyTogetherScore = FAST_FamilyTogetherScore,
            FAST_CaregiverAdvocacyScore = FAST_CaregiverAdvocacyScore, fire_setting = fire_setting, abuse_neglect = abuse_neglect,
            Screening_tool_Trauma = Screening_tool_Trauma, level_of_aggression = level_of_aggression,


                           program = level_pred)#program = Program_suggested,confidence = Confidence


            p.save()
            return HttpResponse(result)
        else:
            form.errors()


            #############
            #- Get predicted values
            #- insert to xxx model
            # if predication is not good:
            #     return HttpResponseRedirect()



        return super().post(request, *args, **kwargs)




    # def get_form(self):
    #     form = super(ModelView,self).get_form()
    #     print(form['Client_code'])

class AdelphoiList(ListCreateAPIView):
    serializer_class = ModelTestsSerializers
    queryset = ModelTests.objects.all()

    def post(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dt = {'Gender': serializer.validated_data.get('gender'),'PrimaryRacecode': serializer.validated_data.get('primaryRaceCode'),
              'CYF_code': serializer.validated_data.get('CYF_code'),'LS_Type': serializer.validated_data.get('ls_type'),
              'EpisodeNumber': serializer.validated_data.get('episode_number'),
              'RefSourceName': serializer.validated_data.get('RefSourceCode'), 'Number of foster care placements': serializer.validated_data.get('number_of_foster_care_placements'),
              'AgeAtEpisodeStart': serializer.validated_data.get('ageAtEpisodeStart'),'Number of prior placements \n(excluding shelter and detention)': serializer.validated_data.get('number_of_prior_placements'),
              'AgeAtEnrollStart': serializer.validated_data.get('ageAtEnrollStart'),
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
              'Abuse, or neglect': serializer.validated_data.get('abuse_neglect'), 'Screening tool for Trauma--Total score': serializer.validated_data.get('Screening_tool_Trauma')
              }


        data = pd.DataFrame(dt, index=[0])

        # data = data.fillna(0)

        Feature_names = ['EpisodeNumber', 'Number of foster care placements', 'AgeAtEpisodeStart',
                         'Number of prior placements \n(excluding shelter and detention)', 'AgeAtEnrollStart',
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

        print("features::", data[Feature_names].shape)
        dummies = pd.DataFrame()
        # print("dummies shape", dummies.shape)

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

        dummies.drop(['CYF_code_3', 'RefSourceName_55'], axis=1, inplace=True)

        print("dummies shape", dummies.shape)
        print(("dumm", dummies.columns))
        Xtest = data[Feature_names]
        Xtest[dummies.columns] = dummies
        print("Xtest shape",Xtest.shape)
        print("xtest columns", Xtest.columns)
        level_model = pickle.load(open("C:/Users/Raghu/Downloads/dt_LR_Level_0.1.sav", "rb"))  # final_dt_48p_263r_2clases_smote.sav
        program_model = pickle.load(open("C:/Users/Raghu/Downloads/dt_T_Program.sav", "rb"))

        level_pred = level_model.predict(Xtest)
        program_pred = program_model.predict(Xtest)
        print(level_pred)
        print("program", program_pred)
        query = Adelphoi_Mapping.objects.filter(program=program_pred, gender=serializer.validated_data.get('gender'), level_of_care=level_pred)

        #######
        location_list = []
        program_list = []
        level_list = []


        for i in query:
            program_list.append(i.program_name)
            level_list.append(i.level_names)
            location_list.append(i.location_names)

        # print(program_list[0])
        # serializer.save(program=program_pred, level_of_care=level_pred)

        sample_dict = {}
        for i in query:
            sample_dict['program_name'] = i.program_name
            sample_dict['level_name'] = i.level_names
            sample_dict['location_names'] = i.location_names

        serializer.save(program=program_pred, level_of_care=level_pred)



        # return JsonResponse({"Message":f'Model is suggesting Program - {str(Program_suggested)} with confidence of {str(round(Confidence * 100, 2))}'}, status=200)

        # return JsonResponse({"Program is":program_list,"level of care":level_list,"locations are":location_list})

        # return Response({"program is":program_list,"level of care is ":level_list},template_name='ad_index.html')

        return render(request,'success_prediction.html',{'question':sample_dict})
    # def perform_create(self, serializer: ModelTestsSerializers):
    #     # try:
    #     dt = {'Gender': serializer.validated_data.get('gender'), 'PrimaryRacecode': serializer.validated_data.get('primaryRaceCode'), 'CYF code': serializer.validated_data.get('CYF_code'), 'LS_Type': serializer.validated_data.get('ls_type'),
    #           'EpisodeNumber': serializer.validated_data.get('episode_number'),
    #           'RefSourceName': serializer.validated_data.get('RefSourceCode'), 'Number of foster care placements': serializer.validated_data.get('number_of_foster_care_placements'),
    #           'AgeAtEpisodeStart': serializer.validated_data.get('ageAtEpisodeStart'),
    #           'Number of prior placements \n(excluding shelter and detention)': serializer.validated_data.get('number_of_prior_placements'),
    #           'AgeAtEnrollStart': serializer.validated_data.get('ageAtEnrollStart'),
    #           'Number of prior treatment terminations (excluding shelter or detention)': serializer.validated_data.get('number_of_prior_treatment_terminations'),
    #           'Length of time since living at home': serializer.validated_data.get('length_of_time_since_living_at_home'),
    #           'Termination directly to AV': serializer.validated_data.get('termination_directly_to_AV'),
    #           'Death Caregiver': serializer.validated_data.get('death_Caregiver'), 'Borderline IQ (below 70)': serializer.validated_data.get('borderline_IQ'),
    #           'Hist of prior program SAO': serializer.validated_data.get('hist_of_prior_program_SAO'),  # hist_of_prior_program_SAO
    #           'Death Silblings': serializer.validated_data.get('death_Silblings'), 'Alcohol Use': serializer.validated_data.get('alcohol_Use'), 'Drug Use': serializer.validated_data.get('drug_Use'),
    #           'Incarcerated caregivers': serializer.validated_data.get('incarcerated_caregivers'),
    #           'Incarcerated siblings': serializer.validated_data.get('incarcerated_siblings'), 'Number of prior AWOLS': serializer.validated_data.get('number_of_prior_AWOLS'),
    #           'Animal cruelty': serializer.validated_data.get('animal_cruelty'),
    #           'Number of prior hospitalizations': serializer.validated_data.get('prior_hospitalizations'),
    #           'Compliant with medication': serializer.validated_data.get('compliant_with_meds'),
    #           'Significant mental health symptoms': serializer.validated_data.get('significant_mental_health_symptoms'),
    #           'Severe mental health symptoms': serializer.validated_data.get('severe_mental_health_symptoms'),
    #           'Autism Diagnosis': serializer.validated_data.get('autism_Diagnosis'), 'Borderline Personality': serializer.validated_data.get('borderline_Personality'),
    #           'Psychosis': serializer.validated_data.get('psychosis'),
    #           'Reactive Attachment Disorder': serializer.validated_data.get('reactive_Attachment_Disorder'), 'Schizophrenia': serializer.validated_data.get('schizophrenia'),
    #           'YLS_PriorCurrentOffenses_Score': serializer.validated_data.get('yls_PriorCurrentOffenses_Score'),
    #           'YLS_FamCircumstances_Score': serializer.validated_data.get('yls_FamCircumstances_Score'),
    #           'YLS_Edu_Employ_Score': serializer.validated_data.get('yls_Edu_Employ_Score'), 'YLS_Peer_Score': serializer.validated_data.get('yls_Peer_Score'),
    #           'YLS_Subab_Score': serializer.validated_data.get('yls_Subab_Score'),
    #           'YLS_Leisure_Score': serializer.validated_data.get('yls_Leisure_Score'), 'YLS_Personality_Score': serializer.validated_data.get('yls_Personality_Score'),
    #           'YLS_Attitude_Score': serializer.validated_data.get('yls_Attitude_Score'), 'Client self-harm': serializer.validated_data.get('client_self_harm'),
    #
    #           'CANS_LifeFunctioning': serializer.validated_data.get('cans_LifeFunctioning'),
    #           'CANS_YouthStrengths': serializer.validated_data.get('cans_YouthStrengths'), 'CANS_CareGiverStrengths': serializer.validated_data.get('cans_CareGiverStrengths'),
    #           'CANS_Culture': serializer.validated_data.get('cans_Culture'),
    #           'CANS_YouthBehavior': serializer.validated_data.get('cans_YouthBehavior'), 'CANS_YouthRisk': serializer.validated_data.get('cans_YouthRisk'),
    #           'CANS_Trauma_Exp': serializer.validated_data.get('cans_Trauma_Exp')
    #
    #           }
    #     data = pd.DataFrame(dt, index=[0])
    #     # print(data.columns)
    #     # print(data.shape)
    #     data = data.fillna(0)
    #     loaded_model = pickle.load(open("C:/Users/Raghu/Downloads/final_dt_48p_263r_2clases_smote.sav", "rb"))
    #     #
    #     results = loaded_model.predict_proba(data)
    #     # print("results::", results)
    #     return results



        #
        # Program_suggested = np.argmax(results[0]) + 1
        # Confidence = results[0][Program_suggested - 1]
        #serializer.save(program=Program_suggested,confidence=Confidence)
        # print(f'Model is suggesting Program - {str(Program_suggested)} with confidence of {str(round(Confidence * 100, 2))}')
        # serializer.save()



