from django.db import models  # type: ignore


class Categorias(models.Model):
    categoria = models.CharField(max_length=30)


class Origem(models.Model):
    origem = models.CharField(max_length=30)


class Periodo(models.Model):
    periodo = models.CharField(max_length=8)


class Planejamento(models.Model):
    grupo = models.CharField(max_length=30)


class Receitas(models.Model):
    descricao = models.CharField(max_length=40)
    data = models.DateField(auto_now=True)
    valor = models.FloatField()
    periodo_id = models.ForeignKey(Periodo, on_delete=models.CASCADE)


class Rec_templates(models.Model):
    descricao = models.CharField(max_length=40)
    valor = models.FloatField()
    dia = models.PositiveSmallIntegerField(max_length=2)


class Despesas(models.Model):
    desc_loja = models.CharField(max_length=40, verbose_name='Estabelecimento')
    desc_desp = models.CharField(max_length=40, verbose_name='Descrição')
    data = models.DateField(auto_now=True)
    valor = models.FloatField()
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE,
                                     verbose_name='Categoria')
    parcela_atual = models.PositiveSmallIntegerField(
        verbose_name='Parcela atual')
    parcelas_total = models.PositiveSmallIntegerField(
        verbose_name='Total de parcelas')
    grupo_id = models.ForeignKey(Planejamento, on_delete=models.CASCADE)
    tipo = models.CharField(default='V', max_length=1,
                            choices=(
                                ('F', 'Fixa'),
                                ('V', 'Variável')))
    origem_id = models.ForeignKey(Origem, on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(Periodo, on_delete=models.CASCADE)


class Desp_fixa(models.Model):
    desc_desp = models.CharField(max_length=100, verbose_name='Descrição')
    dia = models.PositiveSmallIntegerField(max_length=2)
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE,
                                     verbose_name='Categoria')
    valor = models.FloatField()
    grupo_id = models.ForeignKey(Planejamento, on_delete=models.CASCADE)
    origem_id = models.ForeignKey(Origem, on_delete=models.CASCADE)
