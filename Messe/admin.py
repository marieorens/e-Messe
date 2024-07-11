from django.contrib import admin
from .models import Messe


class Mregister(admin.ModelAdmin):
    list_display=("Uid","demandeur","date","heure","intention")
    
    
admin.site.register(Messe,Mregister)

