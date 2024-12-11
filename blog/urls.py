from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal, name='principal'),
    path('post<int:pk>', views.detalle_post, name='detalle_post'),
    path('autor<int:pk>', views.detalle_autor, name='detalle_autor'),
    path('post_new', views.post_new, name="post_new"),
    path('post_edit_<int:pk>', views.post_edit, name="post_edit"),
    path('post/model', views.post_new_model, name="postnewmodel"),
    
]