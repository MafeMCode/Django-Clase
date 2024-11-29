from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal, name='principal'),
    path('post<int:pk>', views.detalle_post, name='detalle_post'),
    path('autor<int:pk>', views.detalle_autor, name='detalle_autor'),
    
]