from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario
class ComentarioSerializar(ModelSerializer):
    class Meta:
        model= Comentario
        fields= ('id','usuario','comentario','data')
