from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from Web.views import IndexTemplateView, UsuariosUpdateView, UsuariosListView


app_name = 'Web'


urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('', IndexTemplateView.as_view(), name='index'),
    path('usuario/', UsuariosListView.as_view(), name='lista_usuario'),
    path('usuario/<id>', UsuariosUpdateView.as_view(), name='atualiza_usuario')
]