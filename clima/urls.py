from django.urls import path, include
from . import views
from clima.views import RetrieveUpdateDestroy, RegistrosListview,CreateRegistro

urlpatterns = [
    path("location",views.index, name='location'),
    path("current/<str:city>",views.current, name='current'),
    path("current/",views.current, name='current'),
    path("prueba",views.prueba, name='prueba'),
    path("delete",views.delete, name='delete'),
    path("registros", RegistrosListview.as_view()),
    path("registros/<pk>", RetrieveUpdateDestroy.as_view()),
    path("consulta",CreateRegistro.as_view()),
    path("consulta/<str:city>",CreateRegistro.as_view()),
    path("all",views.find_all, name='delete'),
    path("delete/<int:id>",views.delete, name='delete'),

]

