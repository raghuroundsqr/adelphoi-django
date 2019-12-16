from rest_framework import serializers
# from rest_framework import ModelTests
from .models import ModelTests

class ModelTestsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ModelTests
        # fields ='__all__'
        exclude = ['modified_date', 'program', 'confidence','level_of_care','facility_type','client_selected_program','client_selected_level','client_selected_facility'] #,,'client_selected_program','client_selected_level','client_selected_facility'

class ModelTestsSerializers_selected_program(serializers.ModelSerializer):

    # ModelTestsSerializers(required=True)


    class Meta:
        model = ModelTests
        fields = ['client_selected_program','client_selected_level','client_selected_facility'] #,'client_selected_level','client_selected_facility'
