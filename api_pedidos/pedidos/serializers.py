from rest_framework import serializers
from .models import Pedido, ItensPedido

class PedidoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Pedido
        fields = ('nome_cliente', 'data_pedido', 'valor_total')

class ItensPedidoSerializers(serializers.ModelSerializer):

    class Meta:
        model = ItensPedido
        fields = ('pedido', 'nome_item', 'quantidade', 'valor_unitario')

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItensPedido.objects.create(pedido=pedido, **item_data)
        return pedido
