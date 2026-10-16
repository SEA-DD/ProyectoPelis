# Miniproyecto 4 – Red de colaboración en el catálogo audiovisual
TecNM / Instituto Tecnológico de Orizaba · Estructuras de Datos · Subconjunto: **Japón**

## Estructura del repositorio
    lista.py           Lista enlazada propia (Nodo + ListaEnlazada) y su TDA
    catalogo.py        Carga/limpieza del CSV y problemas 1, 2 y 3
    medicion.py        Problema 4: enlazada vs list, 3 tamaños -> resultados.csv
    pruebas.py         Pruebas automáticas
    resultados.csv     Salida de la medición empírica
    datos/             netflix_titles.csv (Kaggle: shivamb/netflix-shows)
    docs/              Reporte técnico (Word), guía de práctica y guía de Git
    BITACORA.md        Decisiones de diseño y uso de LLM

## Ejecución (solo requiere Python 3, sin librerías externas)
Desde la carpeta raíz del repositorio:

    python3 pruebas.py
    python3 catalogo.py datos/netflix_titles.csv "Japan" "Takahiro Sakurai"
    python3 medicion.py

## Pregunta guía: ¿qué representación secuencial conviene?
- **Filmografía por director -> lista enlazada propia:** altas y bajas en cualquier posición sin desplazar elementos.
- **Colección completa de títulos y comparación -> list de Python:** acceso por índice y mejor recorrido.
- Año de estreno = clave de orden; duración = minutos (0 si es serie, que reporta temporadas).
- Medición: `list` gana en recorrer y ordenar; ver el reporte en `docs/`.

## Criterios de limpieza
País: Japón aparece entre los países de producción (coproducciones incluidas); se ignoran filas sin año válido y show_id repetidos.

## TDA ListaEnlazada
| Operación | Precondición | Postcondición | Complejidad |
|---|---|---|---|
| insertar_en(pos, x) | 0 ≤ pos ≤ n | x en pos, n+1 | O(n) |
| insertar_ordenado(x) | lista ordenada por año | sigue ordenada | O(n) |
| eliminar_en(pos) | 0 ≤ pos < n | n-1, devuelve el dato | O(n) |
| eliminar_titulo(nombre) | – | quita la primera coincidencia | O(n) |
| contar_y_sumar() | – | (cantidad, minutos) | O(n) |
| contar_y_sumar_rec() | n ≤ 900 | igual resultado | O(n) tiempo y pila |
| ordenar_por_anio() | – | lista nueva ordenada | O(n²) |
