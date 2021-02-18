# Importar librerias
import unittest
from context import scripts

# Carga de datos de funciones y obtencion del diccionario clases_orf
dir_name_functions = '/home/datasci/PycharmProjects/P4-Issam/Data/tb_functions.pl'
clases_orf = scripts.ProcessFiles(dir_name_functions).process_functions()


class TestEjercicio2(unittest.TestCase):
    """
    Clase que contiene suit de test de los resultados del Ejercicio 2
    """

    def test_len_patron(self):
        """
        Test suit para comprobar la longitud de listas ORFs correspondientes a los patrones protein e hydro
        """
        # Obtencion de las lista de ORFs correspondientes a cada patron
        orf_patron_protein, orf_patron_hydro, _, _ = scripts.Ejercicio2.PatronOrf(clases_orf).count_patron()
        # Comprobacio de longitudes de las listas
        self.assertEqual(len(orf_patron_protein), 29)
        self.assertEqual(len(orf_patron_hydro), 112)

    def test_promedios_patrones(self):
        """
        Test suit para comprobar los resultados de los promedios obtenido en el apartado 2.2
        """
        # Obtencion de los promedios
        promedio_1, promedio_2 = scripts.basic.ejercicio_2_2
        # Comprobacion de los valores de los promedios
        self.assertEqual(promedio_1, 5)
        self.assertEqual(promedio_2, 5)


if __name__ == '__main__':
    unittest.main()
