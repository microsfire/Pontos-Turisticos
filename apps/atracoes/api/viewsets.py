from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from apps.atracoes.models import Atracao
from .serializers import AtracaoSerializers


class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'descricao']
