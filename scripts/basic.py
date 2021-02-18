# Importar los modulos del proyecto
from scripts import files_reading, Ejercicio1, Ejercicio2, Ejercicio3, Visualizacion1, Visualizacion2

# Ruta de los conjuntos de datos
dir_name_orfs = '../Data/orfs/'
dir_name_functions = '../Data/tb_functions.pl'

# Lecura de los conjuntos de datos
dic_relacionados = files_reading.ProcessFiles(dir_name_orfs)
dic_clases = files_reading.ProcessFiles(dir_name_functions)

# Obtencion de los diccionarios
relacionados = dic_relacionados.process_file()
clases_orf = dic_clases.process_functions()

# Resultados del Ejercicio 1
ejer1_1 = Ejercicio1.ClasesFuncionales(clases_orf=clases_orf).count_orf()
Ejercicio1.ClasesFuncionales(clases_orf=clases_orf).respiration_orf()

# Resultados del Ejercicio 2
apartado_2_1 = Ejercicio2.PatronOrf(clases_orf=clases_orf).count_patron()
Ejercicio2.PatronOrfRelacionado(relacionados, apartado_2_1).count_relacionados()

# Resultados del Ejercicio3
Ejercicio3.DimensionIdentidad(clases_orf).dimension()

# Visualizaciones
# Grafico Ejercicio 1
Visualizacion1.VisualClasesFuncionales(ejer1_1)
# Graficos Ejercicio 2
_, _, id_patron_protein, id_patron_hydro = apartado_2_1
Visualizacion2.VisualPatron(id_patron_protein,'protein').plotting()
Visualizacion2.VisualPatron(id_patron_hydro,'hydro').plotting()
