from rest_framework import serializers
from .models import Doctor, Region, Clinic, UserInfo, Help


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'
