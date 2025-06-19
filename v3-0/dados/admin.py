from django.contrib import admin  # type: ignore
from . import models  # type: ignore


admin.site.register(models.Categorias)
admin.site.register(models.Origem)
admin.site.register(models.Periodo)
admin.site.register(models.Planejamento)
admin.site.register(models.Receitas)
admin.site.register(models.Rec_templates)
admin.site.register(models.Despesas)
admin.site.register(models.Desp_fixa)
