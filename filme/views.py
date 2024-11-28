# from django.shortcuts import render
from typing import Any
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list -> lista de itens do modelo
    
class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object -> 1 item do modelo
    
    def get(self, request, *args, **kwargs):
        # Descobrir qual o filme ele tá acessando
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs) # Redireciona o usuário para a url final
    
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # Filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context
    
    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ----FUNCTION BASED VIEWS----
# url - view - html
    
# def homepage(request):
#  return render(request, "homepage.html")
    
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)