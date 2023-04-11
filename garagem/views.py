from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from garagem.serializers import MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class =  MarcaSerializer