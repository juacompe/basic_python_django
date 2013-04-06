from rest_framework import serializers
from thestar.models import Competitor

class CompetitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competitor
        fields = ('name', 'no')
