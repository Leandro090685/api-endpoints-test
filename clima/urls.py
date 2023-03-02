from django.urls import path, include
from . import views
from clima.views import RetrieveUpdateDestroy, RegistrosListview,CreateRegistro

urlpatterns = [
    path("registros", RegistrosListview.as_view()),
    path("registros/<pk>", RetrieveUpdateDestroy.as_view()),
    path("consulta",CreateRegistro.as_view()),
    path("consulta/<str:city>",CreateRegistro.as_view()),
    
]

