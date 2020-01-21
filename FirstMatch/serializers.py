from rest_framework import serializers
# from rest_framework import ModelTests
from .models import ModelTests,Adelphoi_Mapping
class ModelTestsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ModelTests
        # fields ='__all__'
        exclude = ['modified_date', 'program','model_program', 'confidence','level_of_care','facility_type','client_selected_program','client_selected_level','client_selected_facility','client_selected_locations',
                   'Program_Completion', 'Returned_to_Care','condition_program'] #,,'client_selected_program','client_selected_level','client_selected_facility'


class Adelphoi_placementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['referred_program','model_program']

class Adelphoi_locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adelphoi_Mapping
        fields = ['location_names']
class UpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        # fields ='__all__'
        exclude = ['client_code','modified_date', 'program', 'model_program', 'confidence', 'level_of_care', 'facility_type',
                   'client_selected_program', 'client_selected_level', 'client_selected_facility',
                   'client_selected_locations',
                   'Program_Completion', 'Returned_to_Care','condition_program']
            # def create(self, validated_data):
    #     return ModelTests.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.number_of_prior_AWOLS = validated_data.get('number_of_prior_AWOLS', instance.number_of_prior_AWOLS)
    #     instance.autism_Diagnosis = validated_data.get('autism_Diagnosis', instance.autism_Diagnosis)
    #     instance.animal_cruelty = validated_data.get('animal_cruelty', instance.animal_cruelty)
    #     instance.referred_program = validated_data.get('referred_program',instance.referred_program)
    #     instance.Exclusionary_Criteria = validated_data.get('Exclusionary_Criteria',instance.Exclusionary_Criteria)
    #     print(instance.Exclusionary_Criteria)
    #     instance.save()
    #     return instance
class ModelTestsSerializers_selected_program(serializers.ModelSerializer):

    # ModelTestsSerializers(required=True)

    class Meta:
        model = ModelTests
        fields = ['client_selected_program','client_selected_level','client_selected_facility','client_selected_locations'] #,'client_selected_level','client_selected_facility'



class ModelTestsSerializer_program_model_suggested(serializers.ModelSerializer):

    class Meta:
        model = ModelTests
        fields = ['client_selected_program','client_selected_level','client_selected_facility','client_selected_locations']


class ProgramSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['client_selected_program']

class LocationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['client_selected_locations']

class ProgramLocationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['client_selected_program','client_selected_locations']


class ProgramLevelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['Program_Completion', 'Returned_to_Care']

class FilterSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = '__all__'

class AdminInterface(serializers.ModelSerializer):
    class Meta:
        model = Adelphoi_Mapping
        fields = '__all__'
        # fields = ['gender','program']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['client_selected_locations']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['client_code','episode_start','episode_number','name','last_name','dob','age','gender','primary_language','RefSourceCode','ls_type','CYF_code',
                  'number_of_prior_placements','number_of_foster_care_placements','number_of_prior_AWOLS','number_of_prior_treatment_terminations','termination_directly_to_AV',
                  'length_of_time_since_living_at_home','hist_of_prior_program_SAO','autism_Diagnosis','borderline_Personality','reactive_Attachment_Disorder','animal_cruelty',
                  'schizophrenia','psychosis','borderline_IQ','significant_mental_health_symptoms','prior_hospitalizations','severe_mental_health_symptoms','compliant_with_meds','Exclusionary_Criteria']


class Test2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTests
        fields = ['incarcerated_caregivers','death_Caregiver','incarcerated_siblings','death_Silblings','alcohol_Use','drug_Use','abuse_neglect','yls_FamCircumstances_Score','yls_Edu_Employ_Score',
                  'yls_Peer_Score','yls_Subab_Score','yls_Leisure_Score','yls_Personality_Score','yls_Attitude_Score','yls_PriorCurrentOffenses_Score','family_support','fire_setting','level_of_aggression',
                  'client_self_harm','Screening_tool_Trauma','cans_LifeFunctioning','cans_YouthStrengths','cans_CareGiverStrengths','cans_Culture','cans_YouthBehavior','cans_YouthRisk',
                  'cans_Trauma_Exp','primaryRaceCode','ageAtEpisodeStart','ageAtEnrollStart','enrollStart_date','english_second_lang','type_of_drugs','FAST_FamilyTogetherScore','FAST_CaregiverAdvocacyScore',
                  'referred_program']

from .models import Musician,Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars')


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'album_musician')

    def create(self, validated_data):
        albums_data = validated_data.pop('album_musician')
        musician = Musician.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=musician, **album_data)
        return musician

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get('release_date', album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
        return instance

