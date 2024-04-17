from django.contrib import admin

from HospitalApp.models import mainpg, Reg

# Register your models here.

# class Reg(admin.ModelAdmin):
#     list_display = ('Name','Age','Gender','Department','Phone','Email')


admin.site.register(mainpg)
admin.site.register(Reg)
