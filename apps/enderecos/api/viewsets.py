from rest_framework import viewsets

from apps.enderecos.models import Endereco
from .serializers import EnderecoSerializers


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializers

