from django.contrib import admin
from .models import Country, State, City, Student, SystemSettings, MarkList


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name', 'country__name',)


admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')
    search_fields = ('name', 'state__name',)


admin.site.register(City, CityAdmin)


class MarkListInline(admin.TabularInline):
    model = MarkList


class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'dob',)

    inlines = [
        MarkListInline
    ]


admin.site.register(Student, StudentAdmin)


class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'website', 'email', 'zipcode')
    search_fields = ('company_name',)


admin.site.register(SystemSettings, SystemSettingsAdmin)
