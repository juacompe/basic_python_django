from thestar.models import Competitor

def create_competitor():
    dee = Competitor()
    dee.name = 'Delilian Alford'
    dee.nick_name = 'Dee'
    dee.no = 1 # vote number
    dee.save()
    return dee

