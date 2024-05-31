from rest_framework import viewsets

from apps.comentarios.models import Comentario
from .serializers import ComentarioSerializers


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializers
