from django.urls import path, include
from . import views
from clima.views import RetrieveUpdateDestroy, RegisterRetrieve

urlpatterns = [
    path("location",views.index, name='location'),
    path("current/<str:city>",views.current, name='current'),
    path("current/",views.current, name='current'),
    path("prueba",views.prueba, name='prueba'),
    path("delete",views.delete, name='delete'),
    path("registros", RetrieveUpdateDestroy.as_view()),
    path("borrar/<pk>", RegisterRetrieve.as_view()),


]

