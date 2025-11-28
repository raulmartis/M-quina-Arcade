import jocs


def main():
    while True: # Bucle principal del menú
        print ("Benvingut/da a l'Arcade") # Missatge de benvinguda
        print ("1. Jugar a Pedra, Paper, Tisora") # Opció de joc 1
        print ("2. Jugar a Endevinar el Número") # Opció de joc 2
        print ("3. Jugar a Llançament de Moneda") # Opció de joc 3
        print ("s. Sortir") # Opció per sortir
        choice=input("Selecciona una de les opcions: ") # Entrada de l'usuari   
        match choice: # Estructura de selecció per a les opcions del menú
            case '1': # Opció per jugar a Pedra, Paper, Tisora
                print("Jugarem al Janken!") # Missatge d'inici del joc
                jocs.janken() # Crida a la funció del joc
                return main()
            case '2': # Opció per jugar a Endevinar el Número
                print("Jugarem a la Nana!") # Missatge d'inici del joc
                jocs.nana() # Crida a la funció del joc
                return main() # Retorna al menú principal després del joc2
            case '3': # Opció per jugar a Llançament de Moneda
                print("Jugarem a Llançament de Moneda!") # Missatge d'inici del joc
                jocs.moneda() # Crida a la funció del joc
                return main()
            case 's': # Opció per sortir del programa
                print("S'acabat el joc. Fins aviat!") # Missatge de sortida
                break # Trenca el bucle per sortir
            case _:
                print("Opció no vàlida. Si us plau, intenta-ho de nou.") # Missatge d'error per opció no vàlida


main()
