from django.urls import path
from . import views

urlpatterns = [
    path(
        route = "update-prueba/",
        view = views.PruebaUpdateView.as_view(),
        name = "update"
    ),
    path(
        route = "prueba-css/",
        view = views.PruebaCss.as_view(),
        name="prueba_css"
    ),
    path(
        route = "prueba-grillas/",
        view = views.PruebaGrillas.as_view(),
        name="prueba_grillas"
    ),
    
]
