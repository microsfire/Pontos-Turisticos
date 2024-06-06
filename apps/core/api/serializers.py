from rest_framework.serializers import ModelSerializer
from apps.core.models import PontoTuristico
from apps.atracoes.api.serializers import AtracaoSerializers
from apps.enderecos.api.serializers import EnderecoSerializers
from apps.comentarios.api.serializers import ComentarioSerializers
from apps.avaliacoes.api.serializers import AvaliacaoSerializers


class PontoTuristicoSerializers(ModelSerializer):
    atracoes = AtracaoSerializers(many=True)
    comentarios = ComentarioSerializers(many=True)
    avaliacoes = AvaliacaoSerializers(many=True)
    endereco = EnderecoSerializers()
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios',
                  'avaliacoes', 'endereco', 'foto']



