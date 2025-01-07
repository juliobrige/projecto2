from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Presentes, Convidados

def home(request):
    if request.method == "GET":
        # Contagem de presentes reservados e não reservados
        nao_reservado = Presentes.objects.filter(reservado=False).count()
        reservado = Presentes.objects.filter(reservado=True).count()
        data = [nao_reservado, reservado]

        # Lista de todos os presentes
        presentes = Presentes.objects.all()

        return render(request, 'home.html', {'presentes': presentes, 'data': data})
    
    elif request.method == "POST":
        nome_presente = request.POST.get('nome_presente')
        foto = request.FILES.get('foto')
        preco = request.POST.get('preco')
        importancia = request.POST.get('importancia')

  

    
        try:
            importancia = int(importancia)
            if importancia < 1 or importancia > 5:
                return HttpResponse("Importância deve estar entre 1 e 5.", status=400)
        except ValueError:
            return HttpResponse("Importância deve ser um número inteiro.", status=400)

      
        presente = Presentes(
            nome_presente=nome_presente,
            foto=foto,
            preco=preco,
            importancia=importancia,
        )
        presente.save()

        return redirect('home')


def lista_convidados(request):
    if request.method == "GET":
   
        convidados = Convidados.objects.all()
        return render(request, 'lista_convidados.html', {'convidados': convidados})
    
    elif request.method == "POST":

        nome_convidado = request.POST.get('nome_convidado')
        whatsapp = request.POST.get('whatsapp')
        maximo_acompanhantes = request.POST.get('maximo_acompanhantes')

        if not nome_convidado:
            return HttpResponse("O nome do convidado é obrigatório.", status=400)

        if not maximo_acompanhantes or not maximo_acompanhantes.isdigit():
            maximo_acompanhantes = 0
        else:
            maximo_acompanhantes = int(maximo_acompanhantes)

      
        convidado = Convidados(
            nome_convidado=nome_convidado,
            whatsapp=whatsapp,
            maximo_acompanhantes=maximo_acompanhantes
        )
        convidado.save()

        return redirect('lista_convidados')
