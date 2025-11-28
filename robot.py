import random # Importa el mòdul random per generar jugades aleatòries

class robot:
    name = "machine" # Nom del robot en aquest cas "machine"
    game = ["pedra","paper","tisora"] # Opcions de joc disponibles: pedra, paper o tisora

    def playing (self):
        choice = random.choice (self.game) # Tria una jugada aleatòria
        return choice # Retorna la jugada aleatòria del robot
class moneda: # Classe principal per al joc de Llançament de Moneda
    name = "npc moneda" # Nom del robot en aquest cas "npc moneda"
    game = ["cara","creu"] # Opcions de joc disponibles: cara o creu

    def jugada (self):
        choice = random.choice (self.game) # Tria una jugada aleatòria
        return choice # Retorna la jugada aleatòria del robot
    