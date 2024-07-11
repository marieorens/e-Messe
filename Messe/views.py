from django.shortcuts import render
from django.http import JsonResponse,HttpRequest,HttpResponse
from .models import Messe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime


def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def forgot(request):
    return render(request, 'forgot.html')

def firstpage(request):
    return render(request, 'firstpage.html')

def acce(request):
    return render(request, 'acceuil.html')

def demande(request):
    return render(request, 'demande.html')

def validation(request):
    return render(request, 'validation.html')

def voirHistorique(request):
    return render(request, 'historique.html')




from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def insert(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        heure = request.POST.get('heure')
        demandeur = request.POST.get('demandeur')
        intention = request.POST.get('intention')
        uid = request.POST.get('uid')
        
        
        if not (date and heure and demandeur and intention and uid):
            return JsonResponse({'error': 'Tous les champs sont requis'}, status=400)

        Messe.objects.create(
            demandeur=demandeur,
            date=date,
            heure=heure,
            intention=intention,
            Uid=uid
        )

        return render(request, 'validation.html') 

    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def __str__(self):
    return f"Messe de {self.demandeur} le {self.date} à {self.heure}"
    
    


def api_get_demandes(request):
    if 'uid' in request.GET:
        user_uid = request.GET['uid']
        historique = Messe.objects.filter(Uid=user_uid).values('demandeur', 'date', 'heure', 'intention')
        return JsonResponse(list(historique), safe=False)
    else:
        return JsonResponse({'error': 'UID manquant dans la requête'}, status=400)
