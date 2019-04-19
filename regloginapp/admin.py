from django.contrib import admin
from .models import  Reg
class Regadmin(admin.ModelAdmin):
    list_display = ['user','fname','lname','dob','mob']
    list_filter = ['dob']
    class meta:
        model=Reg
admin.site.register(Reg,Regadmin)

