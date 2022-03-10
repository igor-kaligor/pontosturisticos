from cgitb import lookup
import imp
from tokenize import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import PontosTuristicos
from rest_framework.decorators import action
from .serializers import PontoTuristicoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PontosTuristicosViewSet(ModelViewSet):

    queryset= PontosTuristicos.objects.all()
    serializer_class=PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao']
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]
    

    #lookup_field='nome'
    #def get_queryset(self):
    #    id=self.request.query_params.get('id',None)
    #    nome=self.request.query_params.get('nome__iexact',None)
    #    descricao=self.request.query_params.get('descricao__iexact',None)
    #    query_set=PontosTuristicos.objects.all()
    #    if id:
    #        query_set=PontosTuristicos.objects.filter(pk=id)
    #    if nome:
    #        query_set.filter(nome=nome)
    #    if descricao:
    #        query_set.filter(descricao=descricao)
    #    return query_set
    
    #------ Sobescrever o GET(list)--------
    #def list(self, request, *args, **kwargs):
    #     return Response({'teste':123})
    #
    #
    #------ Sobescrever o POST(create)--------
    #def create(self, request, *args, **kwargs):
    #    return Response({'nome':request.data['nome']})
    #
    #
    #------ Sobescrever o DELET(destroy)--------
    #def destroy(self, request, *args, **kwargs):
    #    pass 
    # 
    #
    #------ Sobescrever o Retrive(list verbose)--------   
    #def retrieve(self, request, *args, **kwargs):
    #    pass
    #
    #
    #------ Sobescrever o Update(Update Object)--------   
    #def update(self, request, *args, **kwargs):
    #    pass
    #
    #------ Sobescrever o Partial Update(Partial Update)--------   
    #def partial_update(self, request, *args, **kwargs):
    #    pass
    #
    # 
    #     
    #------ Criar actions personalizadas--------   
    #@action(methods=['get'],detail=True)
    #def denunciar(self,request,pk=None):
    #    pass
