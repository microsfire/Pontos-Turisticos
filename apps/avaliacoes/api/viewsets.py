from rest_framework import viewsets

from apps.avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializers


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
