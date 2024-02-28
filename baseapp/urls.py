from django.urls import path
from .views import DoctorListView, RegionListView, ClinicListView, DoctorDetailView, ClinicDetailView, RegionDetailView, \
    ClinicByRegionView, UserInfoView, HelpListView, DoctorsBySpecializationView

urlpatterns = [
    path('doctors/', DoctorListView.as_view()),
    path('doctors/by', DoctorsBySpecializationView.as_view()),
    path('doctor/<int:pk>', DoctorDetailView.as_view()),
    path('regions/', RegionListView.as_view()),
    path('region/<int:pk>', RegionDetailView.as_view()),
    path('clinics/', ClinicListView.as_view()),
    path('clinic/<int:pk>', ClinicDetailView.as_view()),
    path('clinics/by', ClinicByRegionView.as_view()),
    path('helps/', HelpListView.as_view()),
    path('telegram-send/', UserInfoView.as_view()),
]
