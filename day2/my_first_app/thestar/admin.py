from django.contrib import admin
from thestar.models import Competitor, Vote

class CompetitorAdmin(admin.ModelAdmin):
    list_display = ['no', 'nick_name', 'name'] 
    list_display_links = ['no', 'name', 'nick_name'] 

admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Vote)

