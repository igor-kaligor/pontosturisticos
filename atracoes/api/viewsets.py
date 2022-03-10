from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracoes
from .serializers import AtracoesSearializar
from django_filters.rest_framework import DjangoFilterBackend
class AtracoesViewSet(ModelViewSet):
    queryset= Atracoes.objects.all()
    serializer_class= AtracoesSearializar
    filter_fields=('nome','descricao')
 