# Create your views here.
import json
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView

from .models import TestModels,ModelTests#,Mapping_Collection  #,ModelTestSub
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
###

from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from .serializers import ModelTestsSerializers
from rest_framework.parsers import JSONParser

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

            # if ModelTests.objects.filter(client_code=client_code):
            #     print("already exists")
            #     return  super(AboutView).save()
            print(client_code)



            dt = {'Gender': gender, 'PrimaryRacecode': primaryRaceCode, 'CYF code': CYF_code, 'LS_Type': ls_type,
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
                 'CANS_YouthBehavior':cans_YouthBehavior, 'CANS_YouthRisk':cans_YouthRisk, 'CANS_Trauma_Exp': cans_Trauma_Exp

            }

            # 'CANS_LifeFunctioning': cans_LifeFunctioning,
            # 'CANS_YouthStrengths': cans_YouthStrengths, 'CANS_CareGiverStrengths': cans_CareGiverStrengths, 'CANS_Culture': cans_Culture,
            # 'CANS_YouthBehavior': cans_YouthBehavior, 'CANS_YouthRisk': cans_YouthRisk, 'CANS_Trauma_Exp': cans_Trauma_Exp

            data = pd.DataFrame(dt, index=[0])
            # data.to_csv()
            print(data.columns)


            print(data.shape)

            ###
            # data = data.fillna(2)  # remove in front end

            print(data)

            loaded_model = pickle.load(open("C:/Users/Raghu/Downloads/final_dt_48p_263r_2clases_smote.sav", "rb"))

            results = loaded_model.predict_proba(data)
            print("results::", results)

            Program_suggested = np.argmax(results[0]) + 1
            Confidence = results[0][Program_suggested - 1]
            print(f'Model is suggesting Program - {str(Program_suggested)} with confidence of {str(round(Confidence * 100, 2))}')
            result = (f'Model is suggesting Program - {str(Program_suggested)} with confidence of {str(round(Confidence * 100, 2))}')


            # program = Program_suggested
            # q = Adelphoi_Mapping2.objects.all()
            # print(q)

            # ModelTests(program=Program_suggested).save()
            # form.save(commit=False)
            # form.program = Program_suggested

            # mcs = Mapping_Collection.objects.all()
            # # print(q)
            # for mc in mcs:
            #     gender = mc.gender



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

                           program = Program_suggested,confidence = Confidence)
            p.save()
            return HttpResponse(result)


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


    def perform_create(self, serializer: ModelTestsSerializers):
        # try:
        dt = {'Gender': serializer.validated_data.get('gender'), 'PrimaryRacecode': serializer.validated_data.get('primaryRaceCode'), 'CYF code': serializer.validated_data.get('CYF_code'), 'LS_Type': serializer.validated_data.get('ls_type'),
              'EpisodeNumber': serializer.validated_data.get('episode_number'),
              'RefSourceName': serializer.validated_data.get('RefSourceCode'), 'Number of foster care placements': serializer.validated_data.get('number_of_foster_care_placements'),
              'AgeAtEpisodeStart': serializer.validated_data.get('ageAtEpisodeStart'),
              'Number of prior placements \n(excluding shelter and detention)': serializer.validated_data.get('number_of_prior_placements'),
              'AgeAtEnrollStart': serializer.validated_data.get('ageAtEnrollStart'),
              'Number of prior treatment terminations (excluding shelter or detention)': serializer.validated_data.get('number_of_prior_treatment_terminations'),
              'Length of time since living at home': serializer.validated_data.get('length_of_time_since_living_at_home'),
              'Termination directly to AV': serializer.validated_data.get('termination_directly_to_AV'),
              'Death Caregiver': serializer.validated_data.get('death_Caregiver'), 'Borderline IQ (below 70)': serializer.validated_data.get('borderline_IQ'),
              'Hist of prior program SAO': serializer.validated_data.get('hist_of_prior_program_SAO'),  # hist_of_prior_program_SAO
              'Death Silblings': serializer.validated_data.get('death_Silblings'), 'Alcohol Use': serializer.validated_data.get('alcohol_Use'), 'Drug Use': serializer.validated_data.get('drug_Use'),
              'Incarcerated caregivers': serializer.validated_data.get('incarcerated_caregivers'),
              'Incarcerated siblings': serializer.validated_data.get('incarcerated_siblings'), 'Number of prior AWOLS': serializer.validated_data.get('number_of_prior_AWOLS'),
              'Animal cruelty': serializer.validated_data.get('animal_cruelty'),
              'Number of prior hospitalizations': serializer.validated_data.get('prior_hospitalizations'),
              'Compliant with medication': serializer.validated_data.get('compliant_with_meds'),
              'Significant mental health symptoms': serializer.validated_data.get('significant_mental_health_symptoms'),
              'Severe mental health symptoms': serializer.validated_data.get('severe_mental_health_symptoms'),
              'Autism Diagnosis': serializer.validated_data.get('autism_Diagnosis'), 'Borderline Personality': serializer.validated_data.get('borderline_Personality'),
              'Psychosis': serializer.validated_data.get('psychosis'),
              'Reactive Attachment Disorder': serializer.validated_data.get('reactive_Attachment_Disorder'), 'Schizophrenia': serializer.validated_data.get('schizophrenia'),
              'YLS_PriorCurrentOffenses_Score': serializer.validated_data.get('yls_PriorCurrentOffenses_Score'),
              'YLS_FamCircumstances_Score': serializer.validated_data.get('yls_FamCircumstances_Score'),
              'YLS_Edu_Employ_Score': serializer.validated_data.get('yls_Edu_Employ_Score'), 'YLS_Peer_Score': serializer.validated_data.get('yls_Peer_Score'),
              'YLS_Subab_Score': serializer.validated_data.get('yls_Subab_Score'),
              'YLS_Leisure_Score': serializer.validated_data.get('yls_Leisure_Score'), 'YLS_Personality_Score': serializer.validated_data.get('yls_Personality_Score'),
              'YLS_Attitude_Score': serializer.validated_data.get('yls_Attitude_Score'), 'Client self-harm': serializer.validated_data.get('client_self_harm'),

              'CANS_LifeFunctioning': serializer.validated_data.get('cans_LifeFunctioning'),
              'CANS_YouthStrengths': serializer.validated_data.get('cans_YouthStrengths'), 'CANS_CareGiverStrengths': serializer.validated_data.get('cans_CareGiverStrengths'),
              'CANS_Culture': serializer.validated_data.get('cans_Culture'),
              'CANS_YouthBehavior': serializer.validated_data.get('cans_YouthBehavior'), 'CANS_YouthRisk': serializer.validated_data.get('cans_YouthRisk'),
              'CANS_Trauma_Exp': serializer.validated_data.get('cans_Trauma_Exp')

              }
        data = pd.DataFrame(dt, index=[0])
        print(data.columns)
        print(data.shape)
        data = data.fillna(0)
        loaded_model = pickle.load(open("C:/Users/Raghu/Downloads/final_dt_48p_263r_2clases_smote.sav", "rb"))
        #
        results = loaded_model.predict_proba(data)
        print("results::", results)
        #
        Program_suggested = np.argmax(results[0]) + 1
        Confidence = results[0][Program_suggested - 1]
        serializer.save(program=Program_suggested,confidence=Confidence)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except Exception as e:
        #     return Response({"error":"NOT FOUND"},status=404)
