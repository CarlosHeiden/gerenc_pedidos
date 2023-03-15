from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions
from .models import *

# Create your views here.
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers
    permission_classes = [permissions.IsAuthenticated]