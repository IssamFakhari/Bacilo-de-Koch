# Importar librerias
import numpy as np
import re


class ClasesFuncionales:
    """
    Clase para procesar la colección de clases funcionales
    """

    def __init__(self, clases_orf):
        """
        Inits ClasesFuncionales con el diccionario de clases funcionales

        Args:
            clases_orf (:obj:'dict'): diccionario con identificador y descripcion de clases y
                                      ORF,identificdor de la clase y descripción del ORF.
        """
        self.clases_orf = clases_orf

    def count_orf(self):
        """
        Calcula la cantidad de ORFs que pertenecen a cada clase

        Returns:
            new_dict (:obj:'dict'): diccionario con las clases y recuento para cada uno
        """
        # Declaracion del diccionario
        new_dict = {}
        # List comprehension para obtener identificadores de clases uniques (array)
        unique_items = np.unique(
            [self.clases_orf['ORFS'][i]['identificacion_clase'] for i in self.clases_orf['ORFS']])
        # Sumatorio para realizar el recuento para cada identificador
        for item in unique_items:
            new_dict[item] = sum(1 for i in self.clases_orf['ORFS'] if item
                                 in self.clases_orf['ORFS'][i]['identificacion_clase'])

        print('-------------------------------------')
        print('Respuesta del  apartado 1.1')
        print('------------------------------------- \n\n')
        for key, value in new_dict.items():
            print("Clase {} le pertenecen {} ORFs".format(key, value))
        return new_dict

    def respiration_orf(self):
        """
        Calcula los ORFs pertenecientes a la clase con Respiration como descripcion

        Returns:
            recuento (:obj:'int'): entero del calculo que realiza la funcion
        """
        # Declaracion lista con las clases que corresponden a la discripcion
        clase_respiration = []
        # Iteracion sobre los items de 'Clases'
        for key, value in self.clases_orf['Clases'].items():
            # Regex con el valor de la descripcion y marcador para no tener en cuenta
            # si la cadena concuerda con minusculas o mayusculas
            if re.search('respiration', value['descripcion'], re.I):
                clase_respiration.append(key)
        # Sumatorio si se cumple la condicion de clases
        recuento = sum(i for i in self.clases_orf['ORFS'] if
                       clase_respiration == self.clases_orf['ORFS'][i]['identificacion_clase'])

        print('\n\n')
        print('-------------------------------------')
        print('Respuestas del apartado 1.2')
        print('------------------------------------- \n\n', end='\n *')
        print("A la clase {} con la descripción Respiration no le correponde ningun ORF".format(clase_respiration))
