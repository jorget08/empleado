from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path(
        route = "nuevo/",
        view = views.NewDptoYPersonaView.as_view(),
        name = "new"
    ),
    path(
        route = 'lista-departamentos/',
        view = views.DptListView.as_view(),
        name='lista_dpto'
    ),
    
]
