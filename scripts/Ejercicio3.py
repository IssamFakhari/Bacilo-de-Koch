# Importar librerias
import re
import itertools
from operator import itemgetter
from collections import Counter


class DimensionIdentidad:
    """
    Clase para procesar los identificadores de la clase
    """

    def __init__(self, clases_orf):
        """
        Inits DimensionIdentidad con el diccionario de clases funcionales

        Args:
             clases_orf (:obj:'dict'): diccionario con identificador y descripcion de clases y
                                      ORF,identificdor de la clase y descripción del ORF.
        """
        self.clases_orf = clases_orf

    def dimension(self):
        """
        Calcula el numero de clases que tienen como minimo una dimension mayor estricta (>) 0 y
        a la vez multiple de M entre 2 y 9 (ambos incluidos).
        La dimension se refiere a cada uno de los 4 numeros que forman el identificador de clase
        """
        # Declarar lista vacia con para guardar identidades sin corchetes y lista con el recuento
        identidades_clean = []
        recuento = []

        # Guardar las identidad de clase en lista
        identidades_clases = list(self.clases_orf['Clases'].keys())

        for i in identidades_clases:
            # regex para obtener las identidades.Literal de corchetes (\[\]).
            # Cualquier caracter ilimitada longitud (.*?)
            # Replace para eliminar los corchetes
            identidad = re.search('\[(.*?)\]', i).group(0).replace("[", "").replace("]", "")
            identidades_clean.append(identidad)

        # Se recorre los elementos de la lista
        for e in identidades_clean:
            # Conversion del type string de cada dimension de cada identidad en entero
            # Funcion map aplica el cambio de type
            for a in map(int, e.split(',')):
                # Rango M entre 2 y 9
                for i in range(2, 10):
                    # Condicion dimension multiplo de M y mayor que 0
                    if (a % i == 0) and a > 0:
                        recuento.append([i, e])

        # Guardamos los resultados del recuento en un lista de lista
        # Se ordena previamente la lista. Los resultados estan duplicados por lo que hay identidicadores con
        # el mismo M en relacion a un mismo numero
        recuento.sort()
        dimensiones_duplicados = list(recuento for recuento, _ in itertools.groupby(recuento))
        # Diccionario con el entero M y y numero de clases. Se escoge el primero elemento de
        # la lista de listas (M) y se cuenta el numero de ocurrencias.
        dimensiones = dict(Counter(list(map(itemgetter(0), dimensiones_duplicados))))

        # Print de los resultados del ejercicio
        print('\n\n')
        print('-------------------------------------')
        print('Respuestas del ejercicio 3 \n')
        print('-------------------------------------')
        for key, value in dimensiones.items():
            print("M={}: {} clases".format(key, value))