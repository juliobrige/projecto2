from django.shortcuts import render, redirect
from django.http import HttpResponse
from homens.models import Convidados, Presentes

# Visualizar detalhes do convidado e lista de presentes disponíveis
def convidados(request):
    token = request.GET.get('token')
    try:
        convidado = Convidados.objects.get(token=token)  
        presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')  
        return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes})
    except Convidados.DoesNotExist:
        return HttpResponse("Convidado não encontrado.", status=404)


# Responder à presença
def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')

    try:
        convidado = Convidados.objects.get(token=token)  
        if resposta not in ['C', 'R']:
            return redirect(f'/convidados/?token={token}')  
        convidado.status = resposta
        convidado.save()

        return redirect(f'/convidados/?token={token}')  
    except Convidados.DoesNotExist:
        return HttpResponse("Convidado não encontrado.", status=404)


# Reservar presente
def reservar_presente(request, id):
    token = request.GET.get('token')
    
    try:
        convidado = Convidados.objects.get(token=token)  
        presente = Presentes.objects.get(id=id)  

        if presente.reservado:  
            return HttpResponse("Este presente já foi reservado.", status=400)

        
        presente.reservado = True
        presente.reservado_por = convidado
        presente.save()

        return redirect(f'/convidados/?token={token}')  
    except Convidados.DoesNotExist:
        return HttpResponse("Convidado não encontrado.", status=404)
    except Presentes.DoesNotExist:
        return HttpResponse("Presente não encontrado.", status=404)
