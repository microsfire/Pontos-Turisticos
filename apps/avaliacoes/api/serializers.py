from rest_framework.serializers import ModelSerializer
from apps.avaliacoes.models import Avaliacao


class AvaliacaoSerializers(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'user', 'comentario', 'nota']
