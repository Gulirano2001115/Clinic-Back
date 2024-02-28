import requests
from rest_framework import generics
from telegram.constants import ParseMode

from config import settings
from .models import Doctor, Region, Clinic, UserInfo, Help
from .serializers import DoctorSerializer, RegionSerializer, ClinicSerializer, UserInfoSerializer, HelpSerializer


# Doctor
class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# Doctor Detail
class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# Region
class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


# Region Detail
class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


# Clinic
class ClinicListView(generics.ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


# Clinic Detail
class ClinicDetailView(generics.RetrieveAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


# Clinic by Region id
class ClinicByRegionView(generics.ListAPIView):
    serializer_class = ClinicSerializer

    def get_queryset(self):
        region_id = self.request.query_params.get('reg')
        category = self.request.query_params.get('category')
        if region_id and category:
            return Clinic.objects.filter(region_id=region_id, category=category)
        elif region_id:
            return Clinic.objects.filter(region_id=region_id)


class DoctorsBySpecializationView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        category = self.request.query_params.get('specialization')
        if category:
            return Doctor.objects.filter(specialization=category)


# Telegram Bot Send
class UserInfoView(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        telegram_message = f"Yangi bemor :\n\n🏷️ <b><i>Ismi:</i></b> {instance.full_name}\n\n<b><i>Kimga:</i></b> {instance.doctor_name}\n\n🧬 <b><i>Jinsi:</i></b> {instance.gender}\n\n📅 <b><i>Kuni:</i></b> {instance.date}\n\n🕜 <b><i>Soati:</i></b> {instance.time}\n\n🆎 Muammosi: {instance.about}"

        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        params = {'chat_id': chat_id, 'text': telegram_message, 'parse_mode': ParseMode.HTML}

        requests.post(telegram_api_url, params=params)


# Help
class HelpListView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
