from rest_framework import viewsets

from apps.atracoes.models import Atracao
from .serializers import AtracaoSerializers


class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializers