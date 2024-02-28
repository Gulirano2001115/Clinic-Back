from django.contrib import admin
from baseapp.models import Doctor, Region, Clinic, UserInfo, Help

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Region)
admin.site.register(Clinic)
admin.site.register(UserInfo)
admin.site.register(Help)
