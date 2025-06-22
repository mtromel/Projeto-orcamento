from django.db import models  # type: ignore


class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Origem(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Periodo(models.Model):
    periodo = models.CharField(max_length=10)

    def __str__(self):
        return self.periodo


class Planejamento(models.Model):
    grupo = models.CharField(max_length=30)

    def __str__(self):
        return self.grupo


class Receitas(models.Model):
    descricao = models.CharField(max_length=40)
    data = models.DateField(auto_now=True)
    valor = models.FloatField()
    periodo_id = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class RecTemplate(models.Model):
    descricao = models.CharField(max_length=40)
    valor = models.FloatField()
    dia = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.descricao


class Despesas(models.Model):
    desc_loja = models.CharField(max_length=30)
    desc_desp = models.CharField(max_length=40)
    data = models.DateField(auto_now=True)
    valor = models.FloatField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    parcela_atual = models.PositiveSmallIntegerField(default=0)
    parcelas_total = models.PositiveSmallIntegerField(default=0)
    grupo_id = models.ForeignKey(Planejamento, on_delete=models.CASCADE)
    tipo = models.CharField(choices=(('F', 'Fixa'), ('V', 'Variável')),
                            default='V')
    origem_id = models.ForeignKey(Origem, on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.desc_loja} - {self.desc_desp} ({self.valor})"


class DespFixa(models.Model):
    desc_desp = models.CharField(max_length=40)
    dia = models.PositiveSmallIntegerField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.FloatField()
    grupo_id = models.ForeignKey(Planejamento, on_delete=models.CASCADE)
    origem_id = models.ForeignKey(Origem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.desc_desp} ({self.valor})"
