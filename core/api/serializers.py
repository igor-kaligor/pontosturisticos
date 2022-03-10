import re
from rest_framework import serializers
from core.models import PontosTuristicos
from atracoes.api.serializers import AtracoesSearializar
from endereco.api.serializers import EnderecoSearializar
from comentarios.api.serializers import ComentarioSerializar
from avaliacoes.api.serializers import AvaliacaoSerializar
#from rest_framework.fields import SerializerMethodField
class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes= AtracoesSearializar(many=True)
    endereco= EnderecoSearializar()
    comentarios=ComentarioSerializar(many=True)
    avaliacoes=AvaliacaoSerializar(many=True)
    #full=SerializerMethodField()
    class Meta:
        model = PontosTuristicos
        fields = ('id','nome','descricao','foto','atracoes',
        'comentarios','avaliacoes','endereco','full')
    #def full(self,obj):
    #    return '%s - %s' % (obj.nome,obj.descricao)