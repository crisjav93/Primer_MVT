from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import *

def familiar(self):
    familiar_padre = Familia(Nombre='Ariel',Apellido='Schmidt',Email = 'aschmidt@gmail.com', Profesion = 'Arquitecto', Fecha_Nacimiento='1996-10-10')
    familiar_padre.save()
    texto1=f'Familiar {familiar_padre.Nombre} {familiar_padre.Apellido} agregado<p>'

    familiar_madre = Familia(Nombre='Carla',Apellido='Fargo',Email = 'cfargo@gmail.com', Profesion = 'Bioquimica', Fecha_Nacimiento='1993-12-05')
    familiar_madre.save()
    texto2=f'Familiar {familiar_madre.Nombre} {familiar_madre.Apellido} agregado<p>'

    familiar_hijo = Familia(Nombre='Joaquin',Apellido='Schmidt',Email = 'jschmidt@gmail.com', Profesion = 'Estudiante', Fecha_Nacimiento='2015-03-26')
    familiar_hijo.save()
    texto3=f'Familiar {familiar_hijo.Nombre} {familiar_hijo.Apellido} agregado</p>'
        
    texto_muestra = (texto1,texto2,texto3)

    return HttpResponse(texto_muestra)



