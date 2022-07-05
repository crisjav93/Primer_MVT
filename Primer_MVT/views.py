from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import *

def familiar(self):
    familiar = Familia(Nombre='Ariel',Apellido='Schmidt',Email = 'aschmidt@gmail.com', Profesion = 'Arquitecto')
    familiar.save()
    texto=f'Familiar {familiar.Nombre} {familiar.Apellido} agregado'
    return HttpResponse(texto)


