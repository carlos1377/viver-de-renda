import django
from django.conf import settings
import sys
from pathlib import Path
import os
# from random import choice

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

settings.USE_TZ = False

django.setup()


if __name__ == '__main__':
    from vrenda.models import Flow, FlowType, Classification  # type: ignore
    # django_classifications = [
    #     'Receita', 'Investimento', 'Despesa', 'Despesa Futura'
    # ]
    # type_of_flows = ['Receitas', 'Educação', 'Lazer',
    #                  'Necessidades básicas', 'Investimentos']

    # if len(type_of_flows) > 0:
    #     for flow in type_of_flows:
    #         FlowType.objects.create(name=flow)

    # if len(django_classifications) > 0:
    #     for classification in django_classifications:
    #         Classification.objects.create(name=classification)

    # flow_type = FlowType.objects.get(name='Receitas')
    # classification = Classification.objects.get(name='Receita')
    # Flow.objects.create(name='Salário', description='Salário mensal',
    #                     type_of=flow_type, classification=classification)

    flow = Flow.objects.all()
