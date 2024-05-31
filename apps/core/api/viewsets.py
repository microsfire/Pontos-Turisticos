from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.models import PontoTuristico
from .serializers import PontoTuristicoSerializers


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializers

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
       return Response({'test': 123})

    def create(self, request, *args, **kwargs):
        return Response({'ola': request.data['nome']})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    @action(methods=['GET'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'msg': request.data['nome']})

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass







