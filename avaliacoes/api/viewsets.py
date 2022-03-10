from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializar
class AvaliacaoViewSet(ModelViewSet):
    queryset= Avaliacao.objects.all()
    serializer_class= AvaliacaoSerializar
