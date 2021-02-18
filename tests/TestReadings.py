# Importas librerias
import unittest
from context import scripts


class TestReadings(unittest.TestCase):
    """
    Clase que contiene suit de test del procesamiento de datos y el return de los diccionarios

    """

    def test_dict_relacionados(self):
        """
        Test suit para comprobar el contenido del diccionario relacionados
        """

        # Carga de coleccion de datos y obtencion del diccionario
        dir_name_orfs = '/home/datasci/PycharmProjects/P4-Issam/Data/orfs/'
        relacionados = scripts.ProcessFiles(dir_name_orfs).process_file()
        # Declaracion de subconjunto del diccionario original
        mini_dict = {'tb1778': ['tb6', 'tb2936', 'tb1420', 'tb3011', 'tb952', 'tb2102', 'tb670', 'tb2315']}
        # Comprobacion diccionario contiene el subconjunto
        self.assertTrue(mini_dict.items() <= relacionados.items())

    def test_dict_orf(self):
        """
        Test suit para comprobar las claves del diccionario clases_orf
        """
        # Carga de los datos de funciones y obtencion del diccionario clases_orf
        dir_name_functions = '/home/datasci/PycharmProjects/P4-Issam/Data/tb_functions.pl'
        clases_orf = scripts.ProcessFiles(dir_name_functions).process_functions()
        # Declaracion de clases
        claves = ['Clases', 'ORFS']
        # Comprobacion de las claves del diccionario
        self.assertEqual(claves, list(clases_orf.keys()))


if __name__ == '__main__':
    unittest.main()
