import math

print('--------------------------------------------')
print('****** TALLER DE MECÁNICA DE FLUIDO ********')
print('-------------------------------------------- \n')
print('El siguiente programa se diseño para analizar')
print('el sistema de tuberías en paralelo con dos ramas.\n')
print('Se deben usar unidades del Sistema Internacional. \n')


long_tuberia = int(input('Ingrese longitud de la tubería: '))
print('----------------------------------------------------------------------------------------------------------------------------------------')
print('******************************************** F DIMENSIONES DE TUBERÍAS DE ACERO ********************************************************')
print('----------------------------------------------------------------------------------------------------------------------------------------')
print('''Tamaño nom. tubería (pug)        Diametro Exterior(mm)       Espesor de Pared(mm)        Diametro Interior(mm)       Flujo de Área(m^2)        
          1/2                             21.3                       2.77                       15.8                    1.960x10^-4 
          1                               33.4                       3.38                       26.6                    5.574x10^-4     
          2                               60.3                       3.91                       52.5                    2.168x10^-3     
          3                               88.9                       5.49                       77.9                    4.768x10^-3 
          4                               114.3                      6.02                       102.3                   8.213x10^-3  
          5                               141.3                      6.55                       128.2                   1.291x10^-2     
          6                               168.3                      7.11                       154.1                   1.864x10^-2 
          8                               219.1                      8.18                       202.7                   3.226x10^-2
          10                              273.1                      9.27                       254.5                   5.090x10^-2 ''')
print('----------------------------------------------------------------------------------------------------------------------------------------\n')
print('Teniendo encuenta los datos de la tabla anterior...\n')
diam_int_tub_entrada = float(input('Ingrese el diametro interno de la tubería de la entrada: '))
diam_int_tub_salida = float(input('Ingrese el diametro interno de la tubería de la salida: '))
diam_int_tub_ramales = float(input('Ingrese el diametro interno de la tubería de la ramales: '))

while True:
    command = str(input(''' 
        ¿Qué tipo de flujo desea?
            
        [1]Acetona
        [2]Alcohol, etílico
        [3]Alcohol, metílico
        [4]Alcohol, propílico
        [5]Amoniaco, hidratado(25%)
        [6]Benceno
        [7]Tetracloruro de carbono
        [8]Aceite de ricino
        [9]Etilenglicol
        [10]Gasolina
        [11]Glicerina
        [12]Queroseno
        [13]Aceite de linaza
        [14]Mercurio
        [15]Propano

        [c]ontinuar             
    '''))
    if command == '1':
        Graveda_específica = 0.787
        Peso_específico = 7.72
        Densidad = 787
        Viscosidad_dinamica = 0.000316
        Viscosidad_cinematica = 0.000000402
        print('Los valores de Acetona han sido seleccionados')
    elif command == '2':
        Graveda_específica = 0.787
        Peso_específico = 7.72
        Densidad = 787
        Viscosidad_dinamica = 0.001
        Viscosidad_cinematica = 0.00000127
        print('Los valores de Alcohol, etílico han sido seleccionados')
    elif command == '3':
        Graveda_específica = 0.789
        Peso_específico = 7.74
        Densidad = 789
        Viscosidad_dinamica = 0.00056
        Viscosidad_cinematica = 0.00000071
        print('Los valores de Alcohol, metílico han sido seleccionados')
    elif command == '4':
        Graveda_específica = 0.802
        Peso_específico = 7.87
        Densidad = 802
        Viscosidad_dinamica = 0.00192
        Viscosidad_cinematica = 0.00000239
        print('Los valores de Alcohol, propílico han sido seleccionados')
    elif command == '5':
        Graveda_específica = 0.910
        Peso_específico = 8.93
        Densidad = 910
        #Viscosidad_dinamica = 0
        #Viscosidad_cinematica = 0
        print('Los valores de Amoniaco, hidratado(25%) han sido seleccionados')
    elif command == '6':
        Graveda_específica = 0.876
        Peso_específico = 8.59
        Densidad = 876
        Viscosidad_dinamica = 0.000603
        Viscosidad_cinematica = 0.000000688
        print('Los valores de Benceno han sido seleccionados')
    elif command == '7':
        Graveda_específica = 1.590
        Peso_específico = 15.60
        Densidad = 1590
        Viscosidad_dinamica = 0.00091
        Viscosidad_cinematica = 0.000000572
        print('Los valores de Tetracloruro de carbono han sido seleccionados')
    elif command == '8':
        Graveda_específica = 0.960
        Peso_específico = 9.42
        Densidad = 960
        Viscosidad_dinamica = 0.651
        Viscosidad_cinematica = 0.000678
        print('Los valores de Aceite de ricino han sido seleccionados')
    elif command == '9':
        Graveda_específica = 1.100
        Peso_específico = 10.79
        Densidad = 1100
        Viscosidad_dinamica = 0.0162
        Viscosidad_cinematica = 0.0000147
        print('Los valores de Etilenglicol han sido seleccionados')
    elif command == '10':
        Graveda_específica = 0.68
        Peso_específico = 6.67
        Densidad = 680
        Viscosidad_dinamica = 0.000287
        Viscosidad_cinematica = 0.000000422
        print('Los valores de Gasolina han sido seleccionados')
    elif command == '11':
        Graveda_específica = 1.258
        Peso_específico = 12.34
        Densidad = 1258
        Viscosidad_dinamica = 0.960
        Viscosidad_cinematica = 0.000763
        print('Los valores de Glicerina han sido seleccionados')
    elif command == '12':
        Graveda_específica = 0.823
        Peso_específico = 8.07
        Densidad = 823
        Viscosidad_dinamica = 0.00164
        Viscosidad_cinematica = 0.00000199
        print('Los valores de Queroseno han sido seleccionados')
    elif command == '13':
        Graveda_específica = 0.930
        Peso_específico = 9.12
        Densidad = 930
        Viscosidad_dinamica = 0.0331
        Viscosidad_cinematica = 0.0000356
        print('Los valores de Aceite de linaza han sido seleccionados')
    elif command == '14':
        Graveda_específica = 13.54
        Peso_específico = 132.8
        Densidad = 13540
        Viscosidad_dinamica = 0.00153
        Viscosidad_cinematica = 0.000000113
        print('Los valores de Mercurio han sido seleccionados')
    elif command == '15':
        Graveda_específica = 0.495
        Peso_específico = 4.86
        Densidad = 495
        Viscosidad_dinamica = 0.00011
        Viscosidad_cinematica = 0.000000222
        print('Los valores de Propano han sido seleccionados')         
    else:
        break

mat_tuberia_ramal = float(input('Ingrese el material para la tubería del Ramal: '))

mat_tuberia_principal = float(input('Ingrese el material para la tubería del Principal: '))



#def flujo_volum_entrada