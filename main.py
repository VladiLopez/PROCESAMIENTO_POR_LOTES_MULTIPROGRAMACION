#Actividad 4 - Programa 2 - Simular procesamiento por lotes 
#                           con multiprogramación
#Alumnos: López Reynoso Javier Vladimir
#         López Ríos Ian Daniel
                                    # keyboard.read_key  |  msvcrt.kbhit
import os
import time
import random
from pynput import keyboard as kb
from proceso import Proceso

tecla2=""
lista_lotes = []    #[[lote],[lote]] -> lote: [proc, proc, proc, proc]
lotes = []
procesos = []                       #[Op, Res, TME, ID, TT]
listaAux = []
id_usados = []
proc_terminados = []                # [[id, op, res, lote]]      
operador = ['+','-','*','/','%']

contador_global = 0
contadorTiempoTrascurrido = 0
contador_procesos = 0
id_operacion = 1
error = False

def funcionOperacion(operador):
    proceso.numero1 = random.randint(-100, 100)
    proceso.numero2 = random.randint(-100, 100)
    proceso.cadena_operacion = '{} {} {}'.format(proceso.numero1, operador, proceso.numero2)
    procesos.append(proceso.cadena_operacion)        

#------PULSASIONES DEL TECLADO-----------

def pulsa2(letra):
    if letra == kb.KeyCode.from_char('c'):
        return False

def pulsa(tecla):
    global tecla2
    tecla2=""
    tecla2=tecla
    return tecla2



        


cantidad = int(input("Ingrese la cantidad de procesos a realizar: "))

while(contador_procesos < cantidad):

    proceso = Proceso()

    #?Validacion de la operacion        
    while True:
        proceso.operacion = random.choice(operador)
        
        if proceso.operacion == "+":
            funcionOperacion('+')
            proceso.resultado_operacion = proceso.numero1 + proceso.numero2
            procesos.append(proceso.resultado_operacion)
            break

        elif proceso.operacion == "-":
            funcionOperacion('-')
            proceso.resultado_operacion = proceso.numero1 - proceso.numero2
            procesos.append(proceso.resultado_operacion)
            break

        elif proceso.operacion == "*":
            funcionOperacion('*')
            proceso.resultado_operacion = proceso.numero1 * proceso.numero2
            procesos.append(proceso.resultado_operacion)
            break

        elif proceso.operacion == "/":
            proceso.numero1 = random.randint(-100, 100)
            proceso.numero2 = random.randint(-100, 100)
            
            while True:
                if proceso.numero2 == 0:
                    proceso.numero2 = random.randint(-100, 100)
                else:
                    break

            proceso.cadena_operacion = '{} / {}'.format(proceso.numero1, proceso.numero2)
            proceso.resultado_operacion = proceso.numero1 / proceso.numero2
            procesos.append(proceso.cadena_operacion)
            procesos.append(proceso.resultado_operacion)
            break

        elif proceso.operacion == "%":
            proceso.numero1 = random.randint(-100, 100)
            proceso.numero2 = random.randint(-100, 100)
            
            while True:
                if proceso.numero2 == 0:
                    proceso.numero2 = random.randint(-100, 100)
                else:
                    break
            
            proceso.cadena_operacion = '{} % {}'.format(proceso.numero1, proceso.numero2)
            proceso.resultado_operacion = proceso.numero1 / proceso.numero2
            procesos.append(proceso.cadena_operacion)
            procesos.append(proceso.resultado_operacion)
            break

    #?TIEMPO MAXIMO ESTIMADO
    proceso.tiempo_maximo = random.randint(5, 20)
    procesos.append(proceso.tiempo_maximo)

    #?INGRESO DEL ID
    proceso.id_programa = id_operacion
    procesos.append(proceso.id_programa)
    id_operacion = id_operacion + 1

    #?TIEMPO TRANSCURRIDO
    tiempo_transcurrido = 0
    procesos.append(tiempo_transcurrido)

    lotes.append(procesos) # Se agrega el proceso a la lista 'lotes' 
    procesos = [] # Se vacía la lista de procesos para empezar uno nuevo

    contador_procesos += 1

# Se segmentan los lotes (4 procesos por lote)
if len(lotes) % 4 == 0:
    indexI = 0
    indexF = 4

    for proc in range(len(lotes) // 4):
        lista_lotes.append(lotes[indexI:indexF])
        indexI += 4
        indexF += 4

if len(lotes) % 4 != 0:     # En caso de que el numero de procesos no sea divisible entre 4
    indexI = 0
    indexF = 4

    if len(lotes) < 4:
        lista_lotes.append(lotes[indexI:len(lotes)]) #En caso de que sean menos de 4 procesos, el lote se conforma por ese numero
    else:    
        for proc in range(len(lotes) // 4):
            lista_lotes.append(lotes[indexI:indexF])
            indexI += 4
            indexF += 4

        indexF -= 4
        for proc in range(len(lotes) % 4):
            listaAux.append(lotes[indexF+proc])

        lista_lotes.append(listaAux)


os.system("pause")

#Impresion de datos
i = 0

longitudLista = len(lista_lotes)    #Cuantos lotes hay?


while i < longitudLista:    # Longitud de lista lotes (Cuantos lotes hay?)

    j = 0
    longitudProcesos = len(lista_lotes[i])  #Cuantos procesos hay en el lote?
    
    while j < longitudProcesos:  # Longitud de los lotes (Cuantos procesos hay en el lote?)

        contadorTiempoTrascurrido = 0
        tiempoRestante = 1

        while tiempoRestante >= 0:          
            
            tiempoRestante = lista_lotes[i][j][2] - lista_lotes[i][j][4]   #Tiempo restante del proceso -> TME - TT = TR
            contadorTiempoTrascurrido = lista_lotes[i][j][4]

            os.system("cls")      

            print('----------Contador Global----------')
            print(contador_global)

            print('----Cantidad de lotes pendientes---')
            print(len(lista_lotes)-(i+1))

            print('------------Lote Actual------------')
            
            for k in range(j+1, len(lista_lotes[i])):    #Recorrer los procesos del lote   
                print('ID: {} TME: {} TT: {}'.format(lista_lotes[i][k][3],lista_lotes[i][k][2], lista_lotes[i][k][4]), end=' |') 

            print('\n-------Proceso en Ejecucion--------')
            print("Operacion: {} \nTME: {} \nId: {} \nTiempo trascurrido: {} \nTiempo restante: {}".format(lista_lotes[i][j][0], 
            lista_lotes[i][j][2], lista_lotes[i][j][3], contadorTiempoTrascurrido, tiempoRestante))
            
            print('--------Procesos Terminados--------') 
            if len(proc_terminados) >= 0:
            
                for proc in range(len(proc_terminados)):                    
                    print("Id: {} \tOperacion: {} \tResultado: {} \t--> Lote: {}".format(proc_terminados[proc][0],proc_terminados[proc][1],
                    proc_terminados[proc][2], proc_terminados[proc][3])) 

            if tiempoRestante == 0:             
                listaAux = []           
                listaAux.extend([lista_lotes[i][j][3],lista_lotes[i][j][0],lista_lotes[i][j][1], i+1])   #Se agregan los datos a listaAux
                proc_terminados.append(listaAux)
                print("Id: {} \tOperacion: {} \tResultado: {} \t--> Lote: {}".format(lista_lotes[i][j][3],lista_lotes[i][j][0],lista_lotes[i][j][1], i+1))

            
            tiempoRestante -= 1
            contadorTiempoTrascurrido += 1
            lista_lotes[i][j][4] = contadorTiempoTrascurrido        #Actualizar el TR
            contador_global += 1
            time.sleep(0.3) 

            escuchador = kb.Listener(pulsa)
            escuchador.start()

            if tecla2 == kb.KeyCode.from_char('i'):  
                procesoActual = lista_lotes[i][j]                   # Se guarda el proceso actual
                procesoActual[4] = contadorTiempoTrascurrido-1      # Se guarda el tiempo transcurrido
                del lista_lotes[i][j]                               # Se elimina de la lista          
                lista_lotes[i].append(procesoActual)                # Se agrega al final de la lista

            if tecla2 == kb.KeyCode.from_char('e'):
                listaAux = []           
                listaAux.extend([lista_lotes[i][j][3],lista_lotes[i][j][0],'ERROR!', i+1])   #Se agregan los datos a listaAux #!Arreglar index 
                proc_terminados.append(listaAux)

                procesoActual = lista_lotes[i][j]                   # Se guarda el proceso actual


                if j == longitudProcesos-1:     #En caso de que sea el ultimo proceso del lote
                                 
                    if i == longitudLista-1:    # Ultimo proceso del ultimo lote
                        print("Id: {} \tOperacion: {} \tResultado: {} \t--> Lote: {}".format(lista_lotes[i][j][3],lista_lotes[i][j][0],'ERROR!', i+1))
                        # del lista_lotes[i][j]
                        break
                    else:               # Si es el ultimo proceso de algun otro lote  
                        break                    
           
                else:       #Proceso intermedio
                    del lista_lotes[i][j]
                    longitudProcesos -= 1                
                    j = 0
                    
                
            if tecla2 == kb.KeyCode.from_char('p'):
                
                print("\n\tTeclea 'c' para continuar...")

                with kb.Listener(pulsa2) as escucha:
                    escucha.join()

            tecla2 = ''
            letra = ''

        j += 1

    tecla2 = ''
    i += 1