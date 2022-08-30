from http.client import ImproperConnectionState
import math
from random import random

from django.shortcuts import render
from django.contrib.sessions.models import Session

from .forms import cargarArchivoForm

import csv

# Create your views here.


def generator(request):
    if request.method == "POST":
        form = cargarArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            cantidadPreguntas = request.POST.get("cantidadPreguntas")
            if request.FILES["archivo"].name.endswith(".csv"):
                archivo = request.FILES["archivo"].read().decode("utf-8")
                archivo = archivo.splitlines()
                header = archivo[0].split(",")
                archivo = archivo[1:]
                preguntasRandom = []
                for i in range(int(cantidadPreguntas)):
                    pregunta = archivo[int(math.floor(random() * len(archivo)))]
                    archivo.remove(pregunta)
                    pregunta = pregunta.split(",")
                    preguntasRandom.append(pregunta)
                return render(request, "generator.html", {"listaPreguntas": preguntasRandom, "header": header})
            return render(request, "generator.html", {"error": "El archivo no es un CSV", "form": form})

    else:
        form = cargarArchivoForm()
    return render(request, "generator.html", {"form": form})


def test(request):
    return render(request, "test.html")
