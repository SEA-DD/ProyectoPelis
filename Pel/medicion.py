"""Problema 4: lista enlazada propia vs list de Python (3 tamaños de entrada).
Uso: python3 medicion.py   (escribe resultados.csv)"""
import random
import time
from catalogo import Titulo
from lista import ListaEnlazada

TAMANOS = [1000, 2000, 4000]


def tiempo(funcion):
    """Mejor de 3 corridas, en segundos."""
    mejor = 1e9
    for _ in range(3):
        inicio = time.perf_counter()
        funcion()
        mejor = min(mejor, time.perf_counter() - inicio)
    return mejor


random.seed(1)
filas = []
for n in TAMANOS:
    datos = [Titulo("t", random.randint(1950, 2021), 100, [], []) for _ in range(n)]
    enlazada = ListaEnlazada()
    for d in datos:
        enlazada.insertar_final(d)
    arreglo = list(datos)
    extra = datos[0]

    def insertar_enlazada():
        enlazada.insertar_en(n // 2, extra)
        enlazada.eliminar_en(n // 2)

    def insertar_arreglo():
        arreglo.insert(n // 2, extra)
        arreglo.pop(n // 2)

    filas.append([n,
                  tiempo(enlazada.contar_y_sumar),
                  tiempo(lambda: sum(t.minutos for t in arreglo)),
                  tiempo(insertar_enlazada),
                  tiempo(insertar_arreglo),
                  tiempo(enlazada.ordenar_por_anio),
                  tiempo(lambda: sorted(arreglo, key=lambda t: t.anio))])

nombres = ["n", "recorrer_enlazada", "recorrer_list", "insertar_enlazada",
           "insertar_list", "ordenar_enlazada", "ordenar_list"]
print("  ".join(f"{x:>18}" for x in nombres))
for f in filas:
    print(f"{f[0]:>18}  " + "  ".join(f"{x * 1000:>15.4f} ms" for x in f[1:]))
with open("resultados.csv", "w") as salida:
    salida.write(",".join(nombres) + "\n")
    for f in filas:
        salida.write(",".join(str(x) for x in f) + "\n")
