from django.contrib import admin
from .models import CustomUser, Zone, District, AuthCodeFarmer, AuthCodeAgronomist, AuthCodePolicyMaker


# Each model that you want Django to represent in the admin interface needs to be registered.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    # use this for custom view
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')


@admin.register(AuthCodeFarmer)
class AuthCodeFarmerAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'zone')


@admin.register(AuthCodeAgronomist)
class AuthCodeAgronomistAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'zone')


@admin.register(AuthCodePolicyMaker)
class AuthCodePolicyMakerAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'district')
