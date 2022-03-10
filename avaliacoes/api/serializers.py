from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao
class AvaliacaoSerializar(ModelSerializer):
    class Meta:
        model= Avaliacao
        fields= ('id','usuario','comentario','nota','data')

