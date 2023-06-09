# Generated by Django 4.1.7 on 2023-03-30 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_rename_nome_itempedido_produto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='data_pedido',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='itens',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='pedidos.pedido'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='nome_cliente',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='produto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]
