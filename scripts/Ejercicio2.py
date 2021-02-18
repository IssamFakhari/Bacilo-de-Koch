# Importar libreria
import re


class PatronOrf:
    """
    Clase para procesar la colección de clases funcionales
    """
    def __init__(self, clases_orf):
        """
        Inits PatronOrf con el diccionario de clases funcionales

        Args:
             clases_orf (:obj:'dict'): diccionario con identificador y descripcion de clases y
                                      ORF,identificdor de la clase y descripción del ORF.
        """

        # Declaracion de listas vacias que contendra por orden ORFs que cumplen patron hydro y protein
        # e identificaciones de clases que cumplen el patron hydro y patron
        self.clases_orf = clases_orf
        self.orf_patron_hydro = []
        self.orf_patron_protein = []
        self.id_patron_hydro = []
        self.id_patron_protein = []

    def count_patron(self):
        """
        Calcula el numero de clases que contienen como minimo un ORF con los patrones indicados.
        Devuelve las listas de ORFs con el patron indicado.

        Returns:
            orf_patron_protein (:obj:`list`): lista ORFs que cumplen el patron protein
            orf_patron_hydro (:obj:`list`): lista ORFs que cumplen el patron hydro
            id_patron_protein (:obj:`list`): lista con identificaciones de clase que cumplen el patron protein
            id_patron_hydro (:obj:`list`): lista con identificaciones de clase que cumplen el patron hydro
        """

        # Se recorre los elementos ORFs del diccionario
        for key, value in self.clases_orf['ORFS'].items():
            # Regex establece el limite (\b) del termino y longitud ({13}) junto el marcador re.I
            if re.search(r'(?=(\b[a-zA-Z]{13}\b))', value['descripcion'], re.I):
                # contiene el termino hydro
                if re.search('hydro', value['descripcion']):
                    self.id_patron_hydro.append(value['identificacion_clase'])
                    self.orf_patron_hydro.append(key)

            # contiene el termino protein y marcador de min/mayuscla
            if re.search(r'protein', value['descripcion'], re.I):
                self.id_patron_protein.append(value['identificacion_clase'])
                self.orf_patron_protein.append(key)
        print('-------------------------------------')
        print('Respuestas del  apartado 2.1')
        print('------------------------------------- \n\n', end='\n *')

        print('El número de clases que contiene como mínimo un ORF')
        print('con el patrón del término protein es {}'.format(
            len(set(self.id_patron_protein))), end='\n * ')

        print('El número de clases que contiene como mínimo un ORF')
        print('con el patrón del término hydro y 13 caracteres es {} \n\n'.format(
            len(set(self.id_patron_hydro))))

        return self.orf_patron_protein, self.orf_patron_hydro, self.id_patron_protein, self.id_patron_hydro


class PatronOrfRelacionado:
    """
    Clase para procesar la colección de clases funcionales e información sobre los genes indicados
    """

    def __init__(self, relacionados, PatronOrf):
        """
        Inits atronOrfRelacionado con el diccionario con la relación de ORFs y la clase PatronOrf

        Args:
            relacionados (:obj:'dict'): diccionario con la relación de ORFs
            PatronOrf  (:obj:'class'): clase para acceder a los resultados de la funcion count_patron()
        """

        self.relacionados = relacionados
        self.PatronOrf = PatronOrf

    def count_relacionados(self):
        """
        Calculo el numero promedio de ORFs con los cuales se relacionan los ORFs con el patron indicado

        Returns:
            promedio_1 (:obj:`float`): promedio de relacion de ORFs para el patron protein
            promedio_2 (:obj:`float`): promedio de relacion de ORFs para el patron hydro
        """

        # Lista ORFs que cumplen el patron protein e hydro desde la clase PatronOrf
        orf_patron_protein, orf_patron_hydro, _, _ = self.PatronOrf
        # Declaracion variables vacias de recuento de ORF y valores como suma del total de ORFs relacionados
        count = 0
        count_2 = 0
        valores = 0
        valores_2 = 0

        # Se realiza la comprobacion para clave de relacionados (identificacion de ORF)
        # y la lista de ORFs recibidas del patron protein
        for key, value in self.relacionados.items():
            for ide in orf_patron_protein:
                if ide == key:
                    count = count + 1
                    valores += len(value)
        promedio_1 = round((valores / count), 2)
        print('-------------------------------------')
        print('Respuestas del apartado 2.2')
        print('------------------------------------- \n\n', end='\n *')
        print("El promedio en el caso patron protein es {}".format(promedio_1), end='\n * ')

        # Se repite el proceso anterior para patron hydro
        for key, value in self.relacionados.items():
            for ide in orf_patron_hydro:
                if ide == key:
                    count_2 = count_2 + 1
                    valores_2 += len(value)
        promedio_2 = round((valores_2 / count_2), 2)
        print("El promedio en el caso patron hydro es {} \n\n".format(promedio_2))

        return promedio_1, promedio_2
