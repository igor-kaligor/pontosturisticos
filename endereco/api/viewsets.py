from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializers import EnderecoSearializar

class EnderecoViewSet(ModelViewSet):
    queryset= Endereco.objects.all()
    serializer_class=EnderecoSearializar
