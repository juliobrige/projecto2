from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Presentes

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

    elif request.method == "POST":
        nome_presente = request.POST.get('nome_presente')
        preco = request.POST.get('preco')
        importancia = request.POST.get('importancia')
        foto = request.FILES.get('foto')

        # Validação de importância (precisa ser convertida para inteiro)
        try:
            importancia = int(importancia)
            if importancia < 1 or importancia > 10:
                return redirect('home')
        except ValueError:
            return redirect('home')

        

        presentes = Presentes(
        nome_presente =nome_presente,
        preco = preco,
        importancia = importancia,
        foto = foto,)

        presentes.save()

        return redirect('home')
        return HttpResponse(f"Dados recebidos: {nome_presente}, {preco}, {importancia}. Foto: {foto}")

