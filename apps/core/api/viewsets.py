from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissionsOrAnonReadOnly,
    DjangoModelPermissions
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from apps.core.models import PontoTuristico
from .serializers import PontoTuristicoSerializers


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializers
    filter_backends = [SearchFilter]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    lookup_field = 'nome'


    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'msg': request.data['nome']})

    @action(methods=['get'], detail=False)
    def teste(self, request):
        return Response({'msg': 'testando...'})







