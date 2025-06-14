from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import RegiaoAdministrativa, Creche
from .forms import MatriculaForm
from .models import Matricula
from datetime import datetime

def index(request):
    regioes = RegiaoAdministrativa.objects.all()
    return render(request, 'index.html', {'regioes': regioes})

def acompanhamento(request):
    resultado = None
    if request.method == 'POST':
        cpf = request.POST.get('cpf_responsavel')
        nascimento_str = request.POST.get('data_nascimento')
        try:
            nascimento = datetime.strptime(nascimento_str, '%d/%m/%Y').date()
            resultado = Matricula.objects.filter(cpf_responsavel=cpf, data_nascimento=nascimento).first()
        except ValueError:
            resultado = None
    return render(request, 'acompanhamento.html', {'resultado': resultado})

def lista_creches(request):
    ra_id = request.GET.get('ra')
    creches = []
    nome_ra = ''
    page = request.GET.get('page', 1)  

    if ra_id:
        ra = get_object_or_404(RegiaoAdministrativa, id=ra_id)
        nome_ra = ra.nome
        todas_creches = Creche.objects.filter(regiao_id=ra_id, vagas_disponiveis__gt=0).order_by('nome')
        paginator = Paginator(todas_creches, 2)

        creches = paginator.get_page(page)
        
    return render(request, 'creches.html', {
        'creches': creches,
        'nome_ra': nome_ra,
        'ra_id': ra_id,
    })

def matricula(request, creche_id):
    creche = get_object_or_404(Creche, id=creche_id)

    if request.method == 'POST':
        form = MatriculaForm(request.POST, request.FILES)
        if form.is_valid():
            if creche.vagas_disponiveis > 0:
                matricula = form.save(commit=False)
                matricula.creche = creche
                matricula.save()

                creche.vagas_disponiveis -= 1
                creche.save()

                return render(request, 'sucesso.html', {'creche': creche})
    else:
        form = MatriculaForm()

    return render(request, 'matricula_form.html', {'form': form, 'creche': creche})
    


