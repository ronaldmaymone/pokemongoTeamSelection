import csv
import random
import utils
from brkga_mp_ipr.exceptions import LoadError

from pokemon import Pokemon

NAME = 1
TYPE1 = 2
TYPE2 = 3
HP = 5
ATK = 6
DEFE = 7
SPEED_ATK = 8
SPEED_DEF = 9
SPEED = 10
#teamA = []
# teamB = []


class PokeInstance():
    def __init__(self, filename: str):
        self.pokeList = []
        self.teamA = []
        self.typesMatrix = []

        with open(filename,  newline='') as pokemonFile:

            all_poke_info = csv.reader(pokemonFile)
            if not all_poke_info:
                raise LoadError(f"Cannot read file '{filename}'")

            firstLineIgnored = False
            poke_id = 1
            for poke_info in all_poke_info:
                # poke_info é Lista com todas as infos do pokemon
                if firstLineIgnored:
                    # pokeList é a lista de objetos Pokemon
                    pokemon = Pokemon(poke_info[NAME], int(poke_info[HP]), int(poke_info[ATK]), int(poke_info[DEFE]),
                                      int(int(poke_info[SPEED]) + int(poke_info[SPEED_DEF]) + int(poke_info[SPEED_ATK])),
                                      [poke_info[TYPE1], poke_info[TYPE2]])
                    pokemon.id = poke_id
                    self.pokeList.append(pokemon)
                    poke_id += 1
                else:
                    firstLineIgnored = True
        self.readChartFile()

        #teamA é o time de uma instancia do problema
        for i in range(3):
            self.teamA.append(self.pokeList[random.randint(0, 799)])

    def readChartFile(self):
        with open('chart.csv', newline='') as chartFile:
            chartInfo = csv.reader(chartFile)
            for chartRow in chartInfo:
                self.typesMatrix.append(chartRow)

    # only attacking(cp2) pokemon is modified by multiplier
    def battle(self, teamB) -> float:
        battleResult = 0.0
        for pokeA in self.teamA:
            for pokeB in teamB:
                typeMultiplier = self.findBestMultiplier(pokeA.types, pokeB.types)
                battleResult += (pokeB.cp * typeMultiplier) - pokeA.cp
        return battleResult

    def findBestMultiplier(self, typesA, typesB) -> float:
        bestMultiplier = 0.0
        for typeB in typesB:
            for typeA in typesA:
                if (typeA != '') and (typeB != ''):
                    multiplier = float(self.typesMatrix[utils.pickTypeListPos(typeB)][utils.pickTypeListPos(typeA)])
                    if multiplier > bestMultiplier:
                        bestMultiplier = multiplier
        return bestMultiplier
