from django.views.generic import ListView  # type: ignore
from . import models


class IndexView(ListView):
    template_name = 'dados/index.html'
    context_object_name = 'latest_category_list'

    def get_queryset(self):
        return models.Categoria.objects.order_by('-id')[:]


class ConsultaView(ListView):
    model = models.Origem  # TODO: alterar para o modelo correto
    template_name = 'dados/consulta.html'
