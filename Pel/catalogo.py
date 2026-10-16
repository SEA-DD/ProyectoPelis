"""Carga del CSV y solución de los problemas 1, 2 y 3.

Uso:  python3 catalogo.py netflix_titles.csv "Mexico" ["Nombre de actor"]
"""
import csv
import sys
from lista import ListaEnlazada


class Titulo:
    def __init__(self, nombre, anio, minutos, directores, reparto):
        self.nombre = nombre
        self.anio = anio
        self.minutos = minutos          # 0 si es serie (dura "N Seasons")
        self.directores = directores    # list de str
        self.reparto = reparto          # list de str

    def __repr__(self):
        return f"{self.anio} {self.nombre}"


def separar(texto):
    """'A, B, C' -> ['A', 'B', 'C']  (vacío -> [])"""
    return [x.strip() for x in texto.split(",") if x.strip()]


def leer_minutos(texto):
    """'90 min' -> 90.  '2 Seasons' o vacío -> 0."""
    partes = texto.split()
    if len(partes) == 2 and partes[1] == "min":
        return int(partes[0])
    return 0


def cargar(ruta, pais):
    """Lee el CSV y devuelve una list de Titulo del país indicado.
    Limpieza: ignora filas sin año válido y show_id repetidos.
    Criterio: el país aparece entre los países del título (incluye coproducciones).
    """
    titulos = []
    vistos = set()
    with open(ruta, newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            if pais.lower() not in [p.lower() for p in separar(fila["country"])]:
                continue
            if fila["show_id"] in vistos or not fila["release_year"].isdigit():
                continue
            vistos.add(fila["show_id"])
            titulos.append(Titulo(fila["title"], int(fila["release_year"]),
                                  leer_minutos(fila["duration"]),
                                  separar(fila["director"]), separar(fila["cast"])))
    return titulos


# Problema 1: filmografía de cada director, ordenada por año
def construir_filmografias(titulos):
    filmografias = {}                       # director -> ListaEnlazada
    for t in titulos:
        for director in t.directores:
            if director not in filmografias:
                filmografias[director] = ListaEnlazada()
            filmografias[director].insertar_ordenado(t)
    return filmografias


# Problema 3: títulos donde participa un actor
def titulos_de_actor(titulos, actor):
    resultado = ListaEnlazada()
    for t in titulos:
        if actor.lower() in [a.lower() for a in t.reparto]:
            resultado.insertar_ordenado(t)
    return resultado


if __name__ == "__main__":
    titulos = cargar(sys.argv[1], sys.argv[2])
    filmografias = construir_filmografias(titulos)
    print(f"Títulos: {len(titulos)} | Directores: {len(filmografias)}")
    # Problema 2: cantidad y duración acumulada por director (los 10 con más títulos)
    top = sorted(filmografias.items(), key=lambda par: -len(par[1]))[:10]
    for director, lista in top:
        cantidad, minutos = lista.contar_y_sumar()
        print(f"{director}: {cantidad} títulos, {minutos} min -> {list(lista)}")
    if len(sys.argv) > 3:
        lista = titulos_de_actor(titulos, sys.argv[3])
        print(f"\n{sys.argv[3]}: {len(lista)} títulos -> {list(lista)}")
