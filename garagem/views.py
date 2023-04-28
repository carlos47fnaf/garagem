from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca, Cor, Acessorio, Veiculo
from garagem.serializers import MarcaSerializer, CorSerializer, AcessorioSerializer, VeiculoSerializer

class  MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class =  MarcaSerializer

class  CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class =  CorSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer