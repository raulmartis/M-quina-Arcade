import random # Importa el mòdul random per generar números aleatoris
import robot # Importa el mòdul robot per utilitzar la classe robot

def guanyador (jugador, maquina): # Determina el guanyador d'una ronda de Pedra, Paper, Tisora

    if jugador == maquina: # Comprova si hi ha empat entre la màquina o el jugador
        return "empat" # Retorna "empat" si les jugades són iguals
    
    # Aquestes son les regles del joc "Janken" per guanyar.
    if (jugador == "pedra" and maquina == "tisora") or \
       (jugador == "paper" and maquina == "pedra") or \
       (jugador == "tisora" and maquina == "paper"):
        return "jugador" # Retorna "jugador" si el jugador guanya
    
    else: # Retorna "maquina" si la màquina guanya
        return "maquina" # 

#Joc 1: Pedra, Paper, Tisora
def janken (): # Funció principal del joc pedra, paper, tisora
    scorejugador = 0 
    scoremaquina = 0
    ronda_actual = 0

    print ("Pedra, Paper, Tisora") # Títol del joc que es mostrarà a l'inici

    maquina_joc = robot.robot () # Crea una instància del robot per jugar contra ell
    
    # 1. Menú per triar el mode de joc

    while True: # Bucle per triar el mode de joc fins que l'entrada sigui vàlida

        mode = input ("(1: Primer a 3, 2: Millor de 5): ")

        if mode == '1': # Tria el mode "Primer a 3"
            victories_max, rondes_max = 3, float ('inf') # Primer a 3 victòries, rondes il·limitades
            break # Surt del bucle quan l'entrada és vàlida

        elif mode == '2':
            victories_max, rondes_max = float ('inf'), 5 # Millor de 5 rondes, victòries il·limitades
            break # Surt del bucle quan l'entrada és vàlida

        print ("Opció no vàlida.")


    # Bucle principal del joc
    while scorejugador < victories_max and scoremaquina < victories_max and ronda_actual < rondes_max: # Comprova les condicions de finalització del joc
        ronda_actual += 1 # Incrementa la ronda actual 

        print (f"Ronda {ronda_actual} ({scorejugador}-{scoremaquina})") # Això el que fae es mostrar la ronda actual i la puntuació mentre es cumpleixen les condicions del bucle
        
        # 2. Gestió de la jugada de l'usuari al joc
        while True:
            jugada_usuari = input ("La teva jugada (pedra/paper/tisora): ") # Entrada de la jugada de l'usuari

            if jugada_usuari == "pedra" or jugada_usuari == "paper" or jugada_usuari == "tisora": # Comprova si la jugada és vàlida i si es finalitza el bucle
                break # Surt del bucle quan la jugada és vàlida

            print ("Jugada no vàlida.") # Missatge d'error quan la jugada no és vàlida
            
        jugada_maquina = maquina_joc.playing () # Obté la jugada de la màquina
        print (f"Robot: {jugada_maquina}") # Mostra la jugada de la màquina 

        # 3. Comparar i actualitzar puntuacions
        resultat = guanyador (jugada_usuari, jugada_maquina) # Determina el guanyador de la ronda
        
        if resultat == "jugador": # Comprova si el jugador ha guanyat la ronda
            scorejugador += 1 # Incrementa la puntuació del jugador
            print ("Has guanyat la ronda!") 

        elif resultat == "maquina": # Comprova si la màquina ha guanyat la ronda
            scoremaquina += 1 # Incrementa la puntuació de la màquina
            print ("El robot ha guanyat la ronda.")

        else:
            print ("Empat.")
            
    # Final de la partida 
    print ("Fi del Partit") # Missatge de finalització del joc
    
    if scorejugador == scoremaquina: # Comprova si hi ha empat en la partida
        print("Partida acabada en empat.") # Missatge d'empat en la partida
    elif scorejugador > scoremaquina: # Comprova si el jugador ha guanyat la partida
        print("Has guanyat la partida ("+str(scorejugador)+"-"+str(scoremaquina)+")")
    
    else: # Comprova si la màquina ha guanyat la partida
        print("El robot guanya la partida ("+str(scorejugador)+"-"+str(scoremaquina)+")")


#Joc 2: Endevinar el Número
def nana (): # Funció principal del joc endevinar el número
    
    print ("Endevina el Número")
    print ("He pensat un número entre l'1 i el 100.")
    numero_secret = random.randint (1, 100) # Genera un número aleatori entre 1 i 100
    intents = 0 # Inicialitza el comptador d'intents
    
    while True: # Bucle principal del joc
        intent = input ("Introdueix el teu número (o 's' per sortir): ") # Entrada de l'usuari per intentar endevinar el número
      
        if intent == 's': # Comprova si l'usuari vol sortir del joc
            print ("Has decidit sortir del joc. Fins la propera.")
            break
        
        while int(intent) < 1 or int(intent) > 100: # Comprova si el número està dins del rang vàlid
            print ("Número no vàlid. Si us plau, introdueix un número entre l'1 i el 100.") # Missatge d'error per número no vàlid
            intent = input ("Introdueix el teu número (o 's' per sortir): ") # Entrada de l'usuari per intentar de nou
            if intent == 's': # Comprova si l'usuari vol sortir del joc
                print ("Fins aviat has decidit sortir del joc.") # Missatge de sortida del joc
                return
    
        numero_introduit = int (intent) # Converteix l'entrada de l'usuari a enter si no no serà vàlid
        intents += 1  
        if numero_introduit < numero_secret: # Comprova si el número és més alt o més baix que el aleotri per la màquina
            print ("Més alt.")

        elif numero_introduit > numero_secret: # Comprova si el número és més alt o més baix que el aleotri per la màquina
            print ("Més baix.")

        else:
            print (f"Felicitats, has endevinat el número {numero_secret} en {intents} intents.") # Missatge de felicitació quan s'encerta el número 
            break

def moneda (): # Funció principal del joc llançament de moneda 
    
    print ("Llançament de Moneda")
    maquina_moneda = robot.moneda().jugada() # Crea una instància del robot per jugar contra ell

    while True: # Bucle principal del joc
        eleccio_usuari = input ("Tria cara o creu (o 's' per sortir): ") # Entrada de l'usuari per triar cara o creu

        if eleccio_usuari == 's': # Comprova si l'usuari vol sortir del joc
            print ("Has decidit sortir del joc. Fins la propera.")
            break

        if eleccio_usuari != "cara" and eleccio_usuari != "creu" and eleccio_usuari != 's': # Comprova si l'entrada és vàlida
            print ("Elecció no vàlida. Si us plau, tria 'cara' o 'creu'.") # Missatge d'error per elecció no vàlida
            continue 
        
        jugada_maquina = maquina_moneda # Obté la jugada de la màquina
        print (f"Robot: {jugada_maquina}") # Mostra la jugada de la màquina 

        if eleccio_usuari == jugada_maquina: # Comprova si l'usuari ha guanyat
            print ("Has guanyat el llançament de moneda!") # Missatge de victòria de l'usuari
        if eleccio_usuari != jugada_maquina: # Comprova si la màquina ha guanyat
            print ("El robot ha guanyat el llançament de moneda.") # Missatge de victòria de la màquina

if __name__ == "__main__": # Comprova si el script s'està executant directament
    janken()
    nana()
    moneda()