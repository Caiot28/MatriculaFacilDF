from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import RegiaoAdministrativa, Creche
from .forms import MatriculaForm

def index(request):
    regioes = RegiaoAdministrativa.objects.all()
    return render(request, 'index.html', {'regioes': regioes})

"""def lista_creches(request):
    ra_id = request.GET.get('ra')
    creches = []
    if ra_id:
        creches = Creche.objects.filter(regiao_id=ra_id, vagas_disponiveis__gt=0)
    return render(request, 'creches.html', {'creches': creches})"""

def lista_creches(request):
    ra_id = request.GET.get('ra')
    creches = []
    nome_ra = ''
    page = request.GET.get('page', 1)  # página atual (padrão = 1)

    if ra_id:
        ra = get_object_or_404(RegiaoAdministrativa, id=ra_id)
        nome_ra = ra.nome
        todas_creches = Creche.objects.filter(regiao=ra, vagas_disponiveis__gt=0)

        paginator = Paginator(todas_creches, 2)  # 2 creches por página
        creches = paginator.get_page(page)

    return render(request, 'creches.html', {
        'creches': creches,
        'nome_ra': nome_ra,
        'ra_id': ra_id,
    })

"""def matricula(request, creche_id):
    creche = get_object_or_404(Creche, id=creche_id)
    if request.method == 'POST':
        form = MatriculaForm(request.POST, request.FILES)
        if form.is_valid():
            matricula = form.save(commit=False)
            matricula.creche = creche
            matricula.save()
            return render(request, 'sucesso.html')
    else:
        form = MatriculaForm()
    return render(request, 'matricula_form.html', {'form': form, 'creche': creche})"""
def matricula(request, creche_id):
    creche = get_object_or_404(Creche, id=creche_id)

    if request.method == 'POST':
        form = MatriculaForm(request.POST, request.FILES)
        if form.is_valid():
            if creche.vagas_disponiveis > 0:
                matricula = form.save(commit=False)
                matricula.creche = creche
                matricula.save()

                # Atualiza as vagas
                creche.vagas_disponiveis -= 1
                creche.save()

                return render(request, 'sucesso.html')
            # Se não houver vagas não faz nada, volta para o formulário (mantém o form na tela)
    else:
        form = MatriculaForm()

    return render(request, 'matricula_form.html', {'form': form, 'creche': creche})

