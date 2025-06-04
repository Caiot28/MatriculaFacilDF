from django.shortcuts import render, get_object_or_404, redirect
from .models import RegiaoAdministrativa, Creche
from .forms import MatriculaForm

def index(request):
    regioes = RegiaoAdministrativa.objects.all()
    return render(request, 'index.html', {'regioes': regioes})

def lista_creches(request):
    ra_id = request.GET.get('ra')
    creches = []
    if ra_id:
        creches = Creche.objects.filter(regiao_id=ra_id, vagas_disponiveis__gt=0)
    return render(request, 'creches.html', {'creches': creches})

def matricula(request, creche_id):
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
    return render(request, 'matricula_form.html', {'form': form, 'creche': creche})
