# Importar librerias
import unittest
from context import scripts

# Carga de datos de funciones y obtencion del diccionario clases_orf
dir_name_functions = '../Data/tb_functions.pl'
clases_orf = scripts.ProcessFiles(dir_name_functions).process_functions()


class TestEjercicio1(unittest.TestCase):
    """
    Clase que contiene suit de test de los resultados del Ejercicio 1
    """

    def test_len_new_dict(self):
        """
        Test suit para comprobar la longitud del diccionario new_dict
        """
        # Obtencion del diccionario new_dict
        new_dict = scripts.ClasesFuncionales(clases_orf=clases_orf).count_orf()
        # Comprobacion de longitud del diccionario
        self.assertEqual(len(new_dict), 102)

    def test_value_count(self):
        """
        Test suit para comprobar el resultado del apartado 1.2
        """
        # Obtencion del resultado del apartado 1.2
        recuento = scripts.Ejercicio1.ClasesFuncionales(clases_orf=clases_orf).respiration_orf()
        # Comprobacion valor igual a 0
        self.assertEqual(recuento, 0)


if __name__ == '__main__':
    unittest.main()
