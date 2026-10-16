"""Pruebas. Ejecutar: python3 pruebas.py"""
import unittest
from catalogo import Titulo, separar, leer_minutos
from lista import ListaEnlazada


def T(anio, minutos=100, nombre="x"):
    return Titulo(nombre, anio, minutos, [], [])


def anios(lista):
    return [t.anio for t in lista]


class Pruebas(unittest.TestCase):
    def test_insertar_ordenado(self):
        lista = ListaEnlazada()
        for a in (2000, 1990, 2010, 2000, 1980):
            lista.insertar_ordenado(T(a))
        self.assertEqual(anios(lista), [1980, 1990, 2000, 2000, 2010])

    def test_insertar_en(self):
        lista = ListaEnlazada()
        lista.insertar_en(0, T(2)); lista.insertar_en(1, T(4))
        lista.insertar_en(1, T(3)); lista.insertar_en(0, T(1))
        self.assertEqual(anios(lista), [1, 2, 3, 4])
        with self.assertRaises(IndexError):
            lista.insertar_en(9, T(9))

    def test_eliminar(self):
        lista = ListaEnlazada()
        for a in (1, 2, 3, 4):
            lista.insertar_final(T(a, nombre=str(a)))
        self.assertEqual(lista.eliminar_en(0).anio, 1)      # primero
        self.assertEqual(lista.eliminar_en(2).anio, 4)      # último
        self.assertTrue(lista.eliminar_titulo("2"))
        self.assertFalse(lista.eliminar_titulo("99"))
        self.assertEqual(anios(lista), [3])
        lista.eliminar_en(0)
        self.assertEqual(len(lista), 0)

    def test_contar_y_sumar(self):
        lista = ListaEnlazada()
        for a, m in ((1, 90), (2, 100), (3, 110)):
            lista.insertar_final(T(a, m))
        self.assertEqual(lista.contar_y_sumar(), (3, 300))
        self.assertEqual(lista.contar_y_sumar_rec(), (3, 300))
        self.assertEqual(ListaEnlazada().contar_y_sumar_rec(), (0, 0))

    def test_recursion_larga(self):
        lista = ListaEnlazada()
        for a in range(2000):
            lista.insertar_final(T(a))
        with self.assertRaises(RecursionError):
            lista.contar_y_sumar_rec()
        self.assertEqual(lista.contar_y_sumar()[0], 2000)

    def test_ordenar(self):
        lista = ListaEnlazada()
        for a in (5, 3, 9, 1, 3):
            lista.insertar_final(T(a))
        self.assertEqual(anios(lista.ordenar_por_anio()), [1, 3, 3, 5, 9])

    def test_limpieza(self):
        self.assertEqual(separar("A, B,C"), ["A", "B", "C"])
        self.assertEqual(separar(""), [])
        self.assertEqual(leer_minutos("90 min"), 90)
        self.assertEqual(leer_minutos("2 Seasons"), 0)
        self.assertEqual(leer_minutos(""), 0)


unittest.main()
