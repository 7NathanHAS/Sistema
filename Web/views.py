from audioop import reverse
from msilib.schema import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import Usuarios
from django.views.generic.edit import UpdateView
from Sistema.models import Usuarios


# Create your views here.
def index():
    return None


def lista_usuario(request):
    usuario = Usuarios.objetos.all()

    contexto = {'usuario': Usuarios}

    return render(request, "templates/usuario.html", contexto)


class FormularioDeCriacao:
    pass


def cria_usuario(request, pk):
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_usuario'))
        else:
            return render(request, "templates/form.html,", {'form': form})


class ListaUsuarios(ListView):
    template_name = "templates/usuario.html"
    model = Usuarios
    context_object_name = "usuario"


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class UsuariosListView(ListView):
    template_name = "Web/lista.html"
    model = Usuarios
    context_object_name = "funcionarios"


class UsuariosUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Usuarios
    fields = [
        'nome',
        'username',
        'senha'
    ]
