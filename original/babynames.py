#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Ejercicio Baby Names

Definir la función extract_names() de más abajo y cambiar el main()
para que la llame.

Para escribir expresiones regulares, es bueno incluir una copia del texto
objetivo como inspiración.

Aquí hay un ejemplo de cómo se ve el html en los archivos baby.html:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Hitos sugeridos para desarrollo incremental:
 -Extraer el año e imprimirlo
 -Extraer los nombres y números de ranking e imprimirlos
 -Obtener los datos de nombre en un diccionario e imprimirlo
 -Construir la lista [año, 'ranking', ... ] e imprimirla
 -Arreglar main() para utilizar la lista de extract_names
"""

def extract_names(filename):
    """
    Dado un nombre de archivo para baby.html, retorna una lista empezando 
    con la cadena de años seguida del ranking en orden alfabético.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++Tu códico aquí+++
    return


def main():
    # Se provee este código para parseado de la línea de comandos.
    # Hace una lista de los argumentos de la línea de comandos, omitiendo
    # el elemento [0], que es el nombre del mismo script.
    args = sys.argv[1:]

    if not args:
        print 'uso: [--summaryfile] archivo [archivo ...]'
        sys.exit(1)

    # Notar la bandera summary y quitarla de los argumentos.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++Tu código aquí+++
    # Por cada nombre de archivo, obtener los nombres, después imprimir
    # la salida de texto o escribirla a un archivo de sumario (si está la bandera)
    
if __name__ == '__main__':
    main()
