from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.atracoes.models import Atracao
from apps.core.models import PontoTuristico
from apps.atracoes.api.serializers import AtracaoSerializers
from apps.enderecos.api.serializers import EnderecoSerializers
from apps.comentarios.api.serializers import ComentarioSerializers
from apps.avaliacoes.api.serializers import AvaliacaoSerializers


class PontoTuristicoSerializers(ModelSerializer):
    atracoes = AtracaoSerializers(many=True)
    #comentarios = ComentarioSerializers(many=True, read_only=True)
    #avaliacoes = AvaliacaoSerializers(many=True, read_only=True)
    endereco = EnderecoSerializers(read_only=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios',
                  'avaliacoes', 'endereco', 'foto', 'descricao_completa']

        read_only_fields = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)



