import matplotlib.pyplot as plt
import numpy as np
import os


class VisualClasesFuncionales:
    """
    Clase que permite generar visualizacion de de los resultados del Ejercicio 2
    """

    def __init__(self, new_dict):
        """
        Inits VisualClasesFuncionales con el diccionario con el numero de ORFs para cada clase

        Args:
            new_dict (:obj:'dict'): diccionario con las clases y recuento para cada uno
        """

        self.new_dict = new_dict

    def plotting(self):
        """
        Genera grafico  de barras horizontal del numero de ORFs para cada clase

        Returns:
            ('obj':'plot'): guarda el grafico con extension png en la ruta indicada
        """
        # Longitud del eje horizontal
        y_pos = np.arange(len(self.new_dict.keys()))


        # Customizacion grafico
        plt.figure(figsize=(8, 18))
        plt.barh(y_pos, self.new_dict.values(), align='center', height=0.3)
        plt.yticks(y_pos, self.new_dict.keys())

        # Customizacion etiquetas del grafico
        plt.ylabel('Identificador de clase')
        plt.xlabel('Recuento de ORFs')
        plt.title('ORFs por cada clase')
        plt.tight_layout()

        # Guardar grafico
        # Crear directorio para guardar el grafico en el caso de que no exist
        if not os.path.exists('figures'):
            os.mkdir('figures')
        plt.savefig(os.path.join('figures', 'ClasesFuncionales.png'))

