from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        route = "listar-todo-empleados/", 
        view = views.ListAllListView.as_view(), 
        name = "listar-todo"
        ),
    path(
        route = 'listar-dep/<shortname>',
        view = views.ListArea.as_view(),
        name = 'list-dep'
    ),
    path(
        route = "buscar-empleado-palabra/",
        view = views.ListByKeyword.as_view(),
        name = "by-keyword"
    ),
    path(
        route = "buscar-habilidades/",
        view = views.ListaHabilidades.as_view(),
        name = "list-habilidades"
    ),
    path(
        route = 'ver-empleado/<pk>/',
        view = views.EmpleadoDetailView.as_view(),
        name = 'ver-empleado'
    ),
    path(
        route = 'add-empleado/',
        view = views.EmpleadoCreateView.as_view(),
        name = 'add'
    ),
    path(
        route = "update-empleado/<pk>/",
        view = views.EmpleadoUpdateView.as_view(),
        name = "update"
    ),
    path(
        route = "",
        view = views.HomeView.as_view(),
        name = "home"
    ),
    path(
        route = "lista-admin",
        view = views.ListaEmpleadosAdmin.as_view(),
        name = "lista_admin"
    ),
    path(
        route = "delete/<pk>/",
        view = views.EmpleadoDelete.as_view(),
        name = "delete"
    ),
]
