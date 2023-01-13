from django.shortcuts import render, redirect, get_object_or_404
from visitantes.models import Visitante

# Create your views here.
def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        data_visita = request.POST['dataVisita']

        if request.POST['evangelico'] == 'on':
            evangelico = True

        if request.POST['primeiraVez'] == 'on':
            primeira_vez = True

        igreja_origem = request.POST['igrejaOrigem']
        pastor = request.POST['pastor']
        observacao = request.POST['observacao']
        como_conheceu_igreja = request.POST['comoConheceuIgreja']

        visitante = Visitante(nome = nome, email = email, data_visita = data_visita, evangelico = evangelico, primeira_vez = primeira_vez, igreja_origem = igreja_origem, pastor = pastor, observacao = observacao, como_conheceu_igreja = como_conheceu_igreja)
        visitante.save()

        return redirect('pesquisa')
    else:
        return render(request, 'visitantes/cadastro.html')

def pesquisa(request):
    todos_visitantes = Visitante.objects.all()
    return render(request, 'visitantes/pesquisa.html', {'visitantes' : todos_visitantes})

def busca(request, visitante_id):
    visitante = get_object_or_404(Visitante, pk=visitante_id)
    return render(request, 'visitantes/busca.html', {'visitante' : visitante})