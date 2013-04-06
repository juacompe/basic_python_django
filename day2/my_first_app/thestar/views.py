from django.http import HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import generics
from thestar.models import Competitor, Vote
from thestar.serializer import CompetitorSerializer

def home(request):
    template = 'home.html'

    competitors = Competitor.objects.all()
    data = {'competitors': competitors}
    context = RequestContext(request, data)
    return render_to_response(template, context)

def vote(request):
    no = request.GET['no']
    competitor = Competitor.objects.get(no=no)
    new_vote = Vote()
    competitor.votes.add(new_vote)
    return HttpResponse('OK') 

class CompetitorAPI(generics.ListCreateAPIView):
    model = Competitor
    serializer_class = CompetitorSerializer

