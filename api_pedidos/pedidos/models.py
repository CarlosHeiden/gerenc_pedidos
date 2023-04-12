from django.db import models


class Pedido(models.Model):
    nome_cliente = models.CharField(max_length= 100, default=None)
    data_pedido = models.DateField(default=None)
    nome_produto = models. TextField(default=None)
    quantidade = models.IntegerField(default=0)
    vl_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.valor_total = self.quantidade * self.valor_unitario
        super(Pedido, self).save(*args, **kwargs)
