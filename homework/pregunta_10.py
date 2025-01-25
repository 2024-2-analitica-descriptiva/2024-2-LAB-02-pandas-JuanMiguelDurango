"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """



    # Cargar el archivo .tsv
    df = pd.read_csv('./files/input/tbl0.tsv', delimiter='\t')

    # Agrupar por 'c1', ordenar los valores de 'c2', y luego concatenarlos como strings separados por ':'
    df_resultado = df.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()

    # Establecer 'c1' como índice
    df_resultado.set_index('c1', inplace=True)

    # Renombrar la columna para ajustarse al formato solicitado
    df_resultado.rename(columns={'c2': 'c2'}, inplace=True)

    # Mostrar el resultado
    return df_resultado

pregunta_10()