# Importar librerias
import re
import os


class ProcessFiles:
    """
    Clase para procesar las colecciones de datos separadas: tb_functions.pl y orfs/tb_data_0x.pl
    """

    def __init__(self, dir_name):
        """
        Inits ProcessFiles con el path del directorio de ficheros

        Args:
            dir_name (:obj:'strt'): ruta del directorio target
        """
        self.dir_name = dir_name

    def process_file(self):
        """
        Procesa la colección de datos orfs/tb_data_0x.pl, la cual contiene información sobre
        los genes indicados.

        Returns:
            relacionados (:obj:'dict'): diccionario con la relación de ORFs

        """

        # Diccionario vacio para guardar ORF-ORfs relacionados
        relacionados = {}
        # Lectura de ficheros linea a linea
        for i, file_name in enumerate(os.listdir(self.dir_name)):
            with open(os.path.join(self.dir_name, file_name)) as f:
                for line in f:
                    # Captura ORFS únicos y ORFs relacionados mediante regex por el delimitador
                    # Obtiene cualquier caracter (.) ilimitado (*?)
                    # entre parentesis \(\) como caso sensitivo despues del string indicado
                    orf = re.search(r'model\((.*?)\)', line)
                    orf_rel = re.search(r'tb_to_tb_evalue\((.*?)\)', line)
                    # Para evitar repeticion de ORF principales se usa metodo setdefaults()
                    # Se especifica uso de lista para guardar los valores de ORFs relacionados
                    if orf:
                        k = orf.group(1)
                        relacionados.setdefault(k, [])
                    # Seleccionar valor de ORF separando por metodo split indicando el delimitador (',')
                    if orf_rel:
                        v = orf_rel.group(1).split(',', 1)[0]
                        relacionados[k].append(v)
        return relacionados

    def process_functions(self):
        """
        Procesa el fichero tb_functions.pl, el cual contiene infromacion general sobre los genes y
        sus clases funcionales

        Returns:
            clases_orf (:obj:'dict'): diccionario con identificador y descripcion de clases y
                                      ORF,identificdor de la clase y descripción del ORF.
        """

        # Declaracion del diccionario y las claves principales sobre las ques trabajamos
        clases_orf = {'Clases': {}, 'ORFS': {}}

        with open(self.dir_name, 'r') as f:
            for line in f:
                # Regex para los siguientes elementos en orden:identificacion de la clase,
                # descripcion de la clase, ORF, identificacion del orf y descipcion del ORF
                ide_clase = re.search(r'class\((.+?)\)', line)
                desc_clase = re.search(r'class\((.+?)\)', line)
                orf = re.search(r'function\((.+?)\)', line)
                ide_orf = re.search(r'function\((.+?)\)', line)
                desc_orf = re.search(r'function\((.+?)\)', line)

                # Identificacion de clase.Split mediante delimitador (']'),se escoge primer grupo (0)
                # y se añade de nuevo el delimitador.Se establecen identificador unicos
                if ide_clase:
                    ident_clase = ide_clase.group(1).split("]")[0] + str("]")
                    clases_orf['Clases'].setdefault(ident_clase)

                # Descripcion de clase. Metodo replace para guardar valores sin comillas
                if desc_clase:
                    descr_clase = (desc_clase.group(1).split("],")[1]).replace('"', "")
                    clases_orf['Clases'][ident_clase] = {'descripcion': descr_clase}
                # Orf principal. Se establece nested diccionario para guardar los elementos de ORF
                if orf:
                    orfs = orf.group(1).split(",")[0]
                    clases_orf['ORFS'].setdefault(orfs, {})

                # Descripcion de ORF.Metodo replace para guardar valores sin comillas
                if desc_orf:
                    descr_orf = desc_orf.group(1).split("',")[1].replace('"', "")
                    clases_orf['ORFS'][orfs]['descripcion'] = descr_orf
                # Identificacion de ORF. Se repite el mismo metodo como para el identificador de clase
                if ide_orf:
                    ident_orf = str("[") + ide_orf.group(1).split(',[')[1].split(']')[0] + str("]")
                    clases_orf['ORFS'][orfs]['identificacion_clase'] = ident_orf

        return clases_orf
