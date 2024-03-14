"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    suma = 0
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')  # Indica que el delimitador es una tabulación
        for col in reader_csv:
            col_valor = int(col[1])  # Convierte el valor de la columna a entero
            suma += col_valor  # Suma el valor a la variable suma
    return suma
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv
    conteo = {} # Diccionario
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')  # Indica que el delimitador es una tabulación
        for row in reader_csv: # lee fila por fila en el archivo csv
            letra = row[0][0] #mira la primera letra de la primera columna
            if letra in conteo: # condicional para hacer conteo por letra
                conteo[letra] += 1 #si encuentra la letra entonces suma 1
            else:
                conteo[letra] = 1 #sino la cuenta entonces queda con 1
    conteo_ordenado = sorted(conteo.items()) # ordena el diccionario por cada item del conteo
    return conteo_ordenado # el return va al final para devolver el conteo y asignar el diccionario

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv 
    conteo2 = {}  # Diccionario para almacenar la suma de la columna 2 por cada letra de la columna 1
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')  # Indica que el delimitador es una tabulación
        for row in reader_csv:  # Itera sobre cada fila en el archivo CSV
            letra = row[0][0]  # Obtiene la primera letra de la primera columna
            numero = int(row[1])  # se asigna a numero el valor de la segunda columna
            # Suma el número al valor correspondiente a la letra en el diccionario
            if letra in conteo2:
                conteo2[letra] += numero
            else:
                conteo2[letra] = numero
    conteo_ordenado2 = sorted(conteo2.items()) # ordena el diccionario alfabeticamente
    return conteo_ordenado2
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv 
    conteo3 = {}  # Diccionario para almacenar la suma de la columna 3 por cada mes que se repite

    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')  # Indica que el delimitador es una tabulación
        for row in reader_csv:  # Itera sobre cada fila en el archivo CSV
            fecha = row[2]  # se obtiene la fecha completa
            mes = fecha.split("-")[1] #extrae el mes de la fecha ([1] significa que es el primer valor despues del -)
            conteo3[mes] = conteo3.get(mes, 0) + 1 # da el valor del mes y si no existe entonces es 0
    conteo_ordenado3 = sorted(conteo3.items()) # ordena el diccionario alfabeticamente
    return conteo_ordenado3
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv
    conteo5 = {}
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')
        for row in reader_csv:
            letra = row[0] #acceder a la primera columna
            valor = int(row[1])#convertir a entero y acceder a la segunda columna
            if letra in conteo5:
                maximo, minimo = conteo5[letra]
                conteo5[letra] = (max(valor, maximo), min(valor, minimo))
            else:
                conteo5[letra] = (valor, valor)
    return [(letra, maximo, minimo) for letra, (maximo, minimo) in sorted(conteo5.items())]
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    conteo6 = {}
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')
        for row in reader_csv:
            col5 = row[4].split(',')#divide por ','
            for x in col5:
                key,valor = x.split(':')#se separa la clave del valor
                valor = int(valor)
                if key in conteo6:
                    maximo,minimo=conteo6[key]
                    conteo6[key]=(max(valor,maximo),min(valor,minimo))
                else:
                    conteo6[key]=(valor,valor)
    return [(key,maximo,minimo) for key,(minimo,maximo) in sorted(conteo6.items())]
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv
    asociaciones = {}
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')
        for row in reader_csv:
            valor_col2 = int(row[1])
            letra_col1 = row[0]
            if valor_col2 in asociaciones:
                asociaciones[valor_col2].append(letra_col1)
            else:
                asociaciones[valor_col2] = [letra_col1]
    return sorted(asociaciones.items())
def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv
    asociaciones = {}
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')
        for row in reader_csv:
            valor_col2 = int(row[1])
            letra_col1 = row[0]
            if valor_col2 in asociaciones:
                asociaciones[valor_col2].append(letra_col1)
            else:
                asociaciones[valor_col2] = [letra_col1]
    # lista
    lista= []
    for valor, letras in sorted(asociaciones.items()):
        letras_ordenadas = sorted(set(letras))  # Ordenar y eliminar duplicados
        lista.append((valor, letras_ordenadas))
    return lista
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv
    diccionario = {}
    with open("data.csv", newline='') as file:
        reader_csv = csv.reader(file, delimiter='\t')
        for row in reader_csv:
            col5 = row[4].split(',')
            for x in col5:
                key,valor = x.split(':')#se separa la clave del valor
                valor = int(valor)
                if key in diccionario:
                    diccionario[key] += 1
                else:
                    diccionario[key] = 1
    return diccionario     
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import csv
    lista_tuplas = []
    with open("data.csv", newline='') as f:
        reader_csv = csv.reader(f,delimiter="\t")
        for cols in reader_csv:
            letra = cols[0]
            col4_count = len(cols[3].split(','))
            col5_count = len(cols[4].split(','))
            lista_tuplas.append((letra, col4_count, col5_count))
    return lista_tuplas
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv
    resultados = {}
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for row in reader:
            letracol4 = row[3].lower().split(',')  # se convierte la letra en minuscula
            valorcol2 = int(row[1])
            for letra in letracol4:
                letra = letra.strip() # se eliminan los espacios en blanco
                if letra:
                    resultados[letra] = resultados.get(letra, 0) + valorcol2
    sorted_result = dict(sorted(resultados.items()))
    return sorted_result
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    diccionario = {}
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for row in reader:
            col5 = row[4].lower().split(',')  # valores de la col5 separados
            col1 = row[0] #letras de la col1
            for valor in col5:
                key, cantidad = valor.split(':')  # Separar la clave y la cantidad
                cantidad = int(cantidad)
                if col1 in diccionario:
                    diccionario[col1] += cantidad  # Se suma la cantidad a la clave correspondiente
                else:
                    diccionario[col1] = cantidad
    return dict(sorted(diccionario.items()))

