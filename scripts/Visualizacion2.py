# Importar librerias
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os


class VisualPatron:
    """
    Clase que permite generar visualizacion de de los resultados del Ejercicio 2
    """

    def __init__(self, lista_id, patron=None):
        """
        Inits VisualPatron con la lista de identificacion de clases

        Args:
            lista_id (:obj:'list'): lista con identificaciones de clase que cumplen el patron indicado
            patron (:obj:'str'): opcional para indicar el patron de la lista. Por defecto el valor es nulo
        """

        self.lista_id = lista_id
        self.patron = patron

    def data_wrangling(self):
        """
        Transformacion de la lista obtenida. Se obtiene las identificaciones unicas y el recuento

        Returns:
             ides ('obj':'list'): identificaciones unicas de clases que cumplen cada patron
             perc ('obj':'list'): recuento del numero de repeticiones para cada identificacion de clase
        """
        # Metodo Counter que obtiene diccionario con el recuento de las identificaciones
        # Ordenar por items mediante la funcion lambda
        count_lista_id = list(sorted(Counter(self.lista_id).items(), key=lambda item: item[1]))
        # Obtencion desde el array de identicaciones (primer elemento) y recuento (segundo elemento)
        ides = [id_tuple[0] for id_tuple in count_lista_id]
        perc = [id_tuple[1] for id_tuple in count_lista_id]
        return perc, ides

    def percentage_calc(self, pct, allvals):
        """
        Calcula el porcentaje respecto al total de recuentos para cada clase

        Args:
          pct ('obj':'float'): porcentaje respecto al total
          allvals ('obj':'int'): valor del recuento de cada clase

        Returns:
        """
        absolute = int(pct / 100. * np.sum(allvals))
        # Para porcentajes menores de 2 se evita mostrar en el grafico
        if pct > 2:
            return "{:.1f}% ({:d} )".format(pct, absolute)

    def plotting(self):
        """
        Genera grafico circular con el porcentje de ORFs relacionados sobre el total y el numero total

        Returns:
            ('obj':'plot'): guarda el grafico con extension png en la ruta indicada
        """
        # Carga de los datos una vez transformados
        data, categories = self.data_wrangling()
        # Fraccion del radio para compensar el circulo con
        explode = [0.03] * len(data)

        # Customizacion grafico
        # Tamaño de figura y ejes
        fig, ax = plt.subplots(figsize=(8, 18), subplot_kw=dict(aspect="equal"), dpi=140)
        # Grosor de los margenes,texto y obtencion del porcentaje y numero absoluto
        wedges, texts, autotexts = ax.pie(data,
                                          autopct=lambda pct: self.percentage_calc(pct, data),
                                          textprops=dict(color="black"),
                                          pctdistance=0.8,
                                          labeldistance=0.1,
                                          colors=cm.Set1(np.arange(50) / 50.),
                                          startangle=140,
                                          explode=explode)

        # Customizacion leyenda, texto dentro del grafico y titulo
        ax.legend(wedges, categories, title="Identificador de la clase", loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 0.5))
        plt.setp(autotexts, size=9, weight=700)

        # Crear directorio para guardar el grafico en el caso de que no exist
        if not os.path.exists('figures'):
            os.mkdir('figures')
        # Titulo segun el valor del parametro opcional self.patron
        if self.patron == 'protein':
            ax.set_title("%(Nº) de clases con mínimo de 1 ORF con patrón protein")
            # Guardar grafico
            plt.savefig((os.path.join('figures', 'OrfRelacionadosProtein.png')), bbox_inches="tight")

        elif self.patron == 'hydro':
            ax.set_title("%(Nº) de clases con mínimo de 1 ORF con patrón hydro")
            # Guardar grafico
            plt.savefig((os.path.join('figures', 'OrfRelacionadosHydro.png')), bbox_inches="tight")

        else:
            ax.set_title("%(Nº) de clases con mínimo de 1 ORF dado el patrón")