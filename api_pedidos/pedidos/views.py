from rest_framework import viewsets
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['nome_cliente', 'data_pedido']

    def perform_create(self, serializer):
        serializer.save()

