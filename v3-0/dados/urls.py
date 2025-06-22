from django.urls import path  # type: ignore
from . import views


app_name = 'dados'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("consulta/", views.ConsultaView.as_view(), name="consulta"),
]
