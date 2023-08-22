from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca, Cor, Acessorio, Veiculo, Categoria
from garagem.serializers import MarcaSerializer, CorSerializer, AcessorioSerializer, VeiculoSerializer, CategoriaSerializer, VeiculoListSerializer, VeiculoDetailSerializer

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
    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]