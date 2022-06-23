from rest_framework import serializers
from diagnostic.models import Patient, Test

# class PatientSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = Patient
#         fields = ['name', 'email', 'age', 'gender', 'phone', 'selected', 'total_price', 'advance', 'due', 'role']

#     def create(self, validated_data):
#         questions_data = validated_data.pop('selected')
#         quiz = Patient.objects.create(**validated_data)

#         return quiz

# class TestSerializer(serializers.ModelSerializer):
#     selected = PatientSerializer(many=True)
#     class Meta:
#         model = Test
#         fields = ['id', 'name','price']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name','price']


class PatientSerializer(serializers.ModelSerializer):
    selected = TestSerializer(many=True)
    class Meta:
        model = Patient
        fields = ['name', 'email', 'age', 'gender', 'phone', 'selected', 'total_price', 'advance', 'due', 'role']


    def create(self, validated_data):
        tracks_data = validated_data.pop('selected')
        album = Patient.objects.create(**validated_data)

        for track_data in tracks_data:
            Test.objects.create(patient=album, **track_data)

        return album