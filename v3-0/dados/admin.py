from django.contrib import admin  # type: ignore
from . import models


admin.site.register(models.Categoria)
admin.site.register(models.Origem)
admin.site.register(models.Periodo)
admin.site.register(models.Planejamento)
admin.site.register(models.Receitas)
admin.site.register(models.RecTemplate)
admin.site.register(models.Despesas)
admin.site.register(models.DespFixa)
