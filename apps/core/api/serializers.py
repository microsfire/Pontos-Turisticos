from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.atracoes.models import Atracao
from apps.core.models import PontoTuristico, DocIdentificacao
from apps.atracoes.api.serializers import AtracaoSerializers
from apps.enderecos.api.serializers import EnderecoSerializers
from apps.enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializers(ModelSerializer):
    atracoes = AtracaoSerializers(many=True)
    endereco = EnderecoSerializers()
    doc_identificacao = DocIdentificacaoSerializer()
    # Exibe campos extras
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios',
                  'avaliacoes', 'endereco', 'foto', 'descricao_completa', 'descricao_completa2', 'doc_identificacao']

        read_only_fields = ('comentarios', 'avaliacoes')

    # nested serializer com relacionamento ManyToMany
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        # nested serializer com o relacionamento Foreignkey
        endereco = validated_data['endereco']
        del validated_data['endereco']

        # nested serializer com o relacionamento OneToOne
        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        # nested serializer com o relacionamento ManyToMany
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        # nested serializer com o relacionamento Foreignkey
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        # nested serializer com o relacionamento OneToOne
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto
    # Exibe campos extras
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)



