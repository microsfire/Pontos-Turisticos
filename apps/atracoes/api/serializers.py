from rest_framework.serializers import ModelSerializer
from apps.atracoes.models import Atracao


class AtracaoSerializers(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima', 'foto']