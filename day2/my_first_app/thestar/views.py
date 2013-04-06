from django.shortcuts import render_to_response
from thestar.models import Competitor

def home(request):
    template = 'home.html'

    competitors = Competitor.objects.all()
    data = {'competitors': competitors}
    return render_to_response(template, data)

