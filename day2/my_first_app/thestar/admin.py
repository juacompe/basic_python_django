from django.contrib import admin
from thestar.models import Competitor, Vote

class CompetitorAdmin(admin.ModelAdmin):
    list_display = ['no', 'nick_name', 'name'] 
    list_display_links = ['no', 'name', 'nick_name'] 

class VoteAdmin(admin.ModelAdmin):
    list_display = ['competitor'] 
    search_fields = ['competitor__name', 'competitor__nick_name', 
                     'competitor__no'] 


admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(Vote, VoteAdmin)

