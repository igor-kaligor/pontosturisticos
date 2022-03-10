from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco
class EnderecoSearializar(ModelSerializer):
    class Meta:
        model= Endereco
        fields=('id','linha1','linha2','cidade','estado','pais')