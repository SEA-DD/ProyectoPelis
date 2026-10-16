"""Lista simplemente enlazada hecha a mano.

Cada Nodo guarda un dato y una referencia al siguiente nodo:

    primero -> [dato|•] -> [dato|•] -> [dato|None]

TDA ListaEnlazada (operación: complejidad)
    insertar_en(pos, dato) ... O(n)  recorre hasta la posición
    insertar_ordenado(dato) .. O(n)  busca dónde cae el año
    eliminar_en(pos) ......... O(n)
    eliminar_titulo(nombre) .. O(n)
    contar_y_sumar() ......... O(n)  (iterativa, O(1) memoria)
    contar_y_sumar_rec() ..... O(n)  (recursiva, O(n) pila)
    ordenar_por_anio() ....... O(n²) (inserción ordenada elemento por elemento)
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.tamano = 0

    # ---------- insertar ----------
    def insertar_en(self, pos, dato):
        """Pre: 0 <= pos <= tamano.  Post: dato queda en la posición pos."""
        if pos < 0 or pos > self.tamano:
            raise IndexError("posición inválida")
        nuevo = Nodo(dato)
        if pos == 0:                       # caso especial: al inicio
            nuevo.siguiente = self.primero
            self.primero = nuevo
        else:
            anterior = self.primero
            for _ in range(pos - 1):       # llegar al nodo anterior a pos
                anterior = anterior.siguiente
            nuevo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo
        self.tamano += 1

    def insertar_final(self, dato):
        self.insertar_en(self.tamano, dato)

    def insertar_ordenado(self, dato):
        """Pre: la lista ya está ordenada por año.  Post: sigue ordenada."""
        pos = 0
        actual = self.primero
        while actual is not None and actual.dato.anio <= dato.anio:
            actual = actual.siguiente
            pos += 1
        self.insertar_en(pos, dato)

    # ---------- eliminar ----------
    def eliminar_en(self, pos):
        """Pre: 0 <= pos < tamano.  Devuelve el dato eliminado."""
        if pos < 0 or pos >= self.tamano:
            raise IndexError("posición inválida")
        if pos == 0:
            borrado = self.primero
            self.primero = borrado.siguiente
        else:
            anterior = self.primero
            for _ in range(pos - 1):
                anterior = anterior.siguiente
            borrado = anterior.siguiente
            anterior.siguiente = borrado.siguiente   # saltarse el nodo
        self.tamano -= 1
        return borrado.dato

    def eliminar_titulo(self, nombre):
        """Elimina el primer título con ese nombre. Devuelve True si lo halló."""
        pos = 0
        actual = self.primero
        while actual is not None:
            if actual.dato.nombre == nombre:
                self.eliminar_en(pos)
                return True
            actual = actual.siguiente
            pos += 1
        return False

    # ---------- recorrer ----------
    def contar_y_sumar(self):
        """Devuelve (cantidad de títulos, minutos acumulados). Iterativa."""
        cantidad = 0
        minutos = 0
        actual = self.primero
        while actual is not None:
            cantidad += 1
            minutos += actual.dato.minutos
            actual = actual.siguiente
        return cantidad, minutos

    def contar_y_sumar_rec(self):
        """Lo mismo, pero recursiva. Falla con ~1000 nodos (límite de Python)."""
        if self.tamano > 900:
            raise RecursionError("lista demasiado larga para recursión")
        return _contar_rec(self.primero)

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __len__(self):
        return self.tamano

    # ---------- ordenar ----------
    def ordenar_por_anio(self):
        """Devuelve una lista nueva ordenada, insertando uno por uno."""
        nueva = ListaEnlazada()
        for dato in self:
            nueva.insertar_ordenado(dato)
        return nueva


def _contar_rec(nodo):
    if nodo is None:                              # caso base: no hay más nodos
        return 0, 0
    cantidad, minutos = _contar_rec(nodo.siguiente)   # caso recursivo
    return cantidad + 1, minutos + nodo.dato.minutos
