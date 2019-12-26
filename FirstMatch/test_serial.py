from rest_framework import serializers
# from rest_framework import ModelTests
from .models import ModelTests

class ModelTestsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ModelTests
        # fields ='__all__'
        exclude = ['modified_date', 'program', 'confidence','level_of_care','facility_type','client_selected_program','client_selected_level','client_selected_facility','client_selected_locations','Program_Completion', 'Returned_to_Care']

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