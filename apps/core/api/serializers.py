from rest_framework.serializers import ModelSerializer
from apps.core.models import PontoTuristico


class PontoTuristicoSerializers(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto']



