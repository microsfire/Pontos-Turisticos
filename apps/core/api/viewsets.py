from rest_framework import viewsets

from apps.core.models import PontoTuristico
from .serializers import PontoTuristicoSerializers


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializers


