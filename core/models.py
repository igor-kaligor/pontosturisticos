from distutils.command.upload import upload
from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

class PontosTuristicos(models.Model):
    nome= models.CharField(max_length=150)
    descricao= models.TextField()
    aprovado=models.BooleanField(default=False)
    atracoes= models.ManyToManyField(Atracoes)
    comentarios= models.ManyToManyField(Comentario)
    avaliacoes= models.ManyToManyField(Avaliacao)
    endereco= models.ForeignKey(Endereco,on_delete=models.CASCADE, null=True, blank=True)
    foto= models.ImageField(upload_to='pontos_turisticos',null=True,blank=True)
    
    @property
    def full(self):
        return '%s - %s' % (self.nome,self.descricao)

    def __str__(self):
        return self.nome
    



