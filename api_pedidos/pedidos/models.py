from django.db import models

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=80)
    data_pedido = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_cliente

class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nome_item = models.CharField(max_length=70)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.pedido