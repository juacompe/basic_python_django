from thestar.models import Competitor

def create_competitor(name='Delilian Alford', nick_name='Dee', no=1):
    dee, is_created = Competitor.objects.get_or_create(
        name=name, nick_name=nick_name, no=no)
    return dee

