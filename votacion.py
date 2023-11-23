#Inicialización de las listas
candidatos = ['Santiago','Milei','Putin','Blanco']
contadores = [0,0,0,0]
votantes = []
votosF = []

#Creamos la clase de votacion

class Votacion:
    def __init__(self, idVotante, numCandidato): #Se define el constructor
        self.idVotante = idVotante
        self.numCandidato = numCandidato

    def agregarVotante(idVotante): #Creamos una función para agregar a los aprendices que van a votar
        if idVotante not in votantes:
            votantes.append(idVotante)
            print(f'\nEl aprendiz con documento {idVotante} se agrego exitosamente :D.')
        else:
            print(f'\nEl aprendiz con documento {idVotante} ya se encuentra registrado.')

    def validarVotante(idVotante): #Creamos un función para validar  si el aprendiz ya voto
        if idVotante in votosF:
            print(f'\nEl aprendiz {idVotante} ya ha votado')
        elif idVotante in votantes:
            print('\nLos candidatos a vocería de este año son:\n-Santiago con el tarjeton 1\n-Milei con el tarjeton 2\n-Putín con el tarjeton 3\n-Voto en blanco con el tarjeton 4')
            
            def votos(idVoto,numCandidato): #Creamos una función para registrar los votos 
                
                votosF.append(idVotante)

                if numCandidato == 1:
                    contadores[0] += 1
                elif numCandidato == 2:
                    contadores[1] += 1
                elif numCandidato == 3:
                    contadores[2] += 1
                elif numCandidato == 4:
                    contadores[3] += 1
                else:
                    print(f'\nEl candidato {numCandidato} no existe. :v')

            votos(idVoto = idVotante, numCandidato=int(input('\nIngrese el numero del targeton del candidato: ')))
                
        else:
            print(f'\nEl aprendiz con documento {idVotante} no se encuentra registrado.')

    def finalizarVotacion(): #Creamos una función para mostrar los resultados de la votación
        print(f'\nResultados de la votación:\n\nSantiago: {contadores[0]}\nMilei: {contadores[1]}\nPutín: {contadores[2]}\nVoto en Blanco:{contadores[3]}')
        
        
        if contadores[0] == contadores[1]:
            print(f'\nLos candidatos Santiago y Milei quedaron empatados con {contadores[0]} votos. ')
        elif contadores[0] == contadores[2]:
            print(f'\nLos candidatos Santiago y Putín quedaron empatados con {contadores[0]} votos.')
        elif contadores[0] == contadores[3]:
            print(f'\nLos candidatos Santiago y Voto en blanco quedaron empatados con {contadores[0]} votos')
        elif contadores[1] == contadores[2]:
            print(f'\nLos cadidatos Milei y Putín quedaron enpatados con {contadores[1]} votos.')
        elif contadores[1] == contadores[3]:
            print(f'\nLos cadidatos Milei y Voto en blanco quedaron enpatados con {contadores[1]} votos.')
        elif contadores[2] == contadores[3]:
            print(f'\nLos cadidatos Putín y Voto en blanco quedaron enpatados con {contadores[2]} votos')
        else:
            ganador = max(contadores)
            indGanador = contadores[ganador]
            nombreGanador = candidatos[indGanador]

            print(f'\nEl ganador de las votaciónes es {nombreGanador} con {ganador} votos')

#Ejecución del programa

while True: #Menu
    print('\n\nBienvenido al sistema de votaciones, ingrese:\n-1 para registrarse\n-2 para votar\n-3 para ver los resultados de las votaciones\n-0 para salir')

    opc = int(input('\nIngrese la opción aqui: '))
    
    if opc == 0: #Opcion 0 para salir
        break
    elif opc == 1: #Opcion 1 para registrar votantes
        Votacion.agregarVotante(int(input('\nIngrese su n° de identificación: ')))
    elif opc == 2: #Opcion 2 para ingresar un voto
        Votacion.validarVotante(int(input('\nIngrese su n° de identificación: ')))
    elif opc == 3: #Opción para mostrar resultados de la votación
        Votacion.finalizarVotacion()
    else:
        print(f'\n{opc} no es una opción valida')