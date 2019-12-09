from rest_framework import serializers
# from rest_framework import ModelTests
from .models import ModelTests

class ModelTestsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ModelTests
        # fields ='__all__'
        exclude = ['modified_date', 'program', 'confidence','level_of_care']



    # def create(self, validated_data):
    #     print('vd:', validated_data)
    #
    #
    #
    #     return validated_data