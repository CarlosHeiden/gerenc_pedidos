from rest_framework import serializers
from .models import *



class PedidoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Pedido
        fields = '__all__'

    