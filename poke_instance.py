import csv

from brkga_mp_ipr.exceptions import LoadError

from pokemon import Pokemon

NAME = 1
TYPE1 = 2
TYPE2 = 3
HP = 5
ATK = 6
DEFE = 7
SPEED = 10
#teamA = []
# teamB = []


class PokeInstance():
    def __init__(self, filename: str):
        self.pokeList = []
        self.teamA = []

        with open(filename,  newline='') as pokemonFile:

            all_poke_info = csv.reader(pokemonFile)

            firstLineIgnored = False
            poke_id = 1
            for poke_info in all_poke_info:
                # poke_info é Lista com todas as infos do pokemon
                if firstLineIgnored:
                    # pokeList é a lista de objetos Pokemon
                    pokemon = Pokemon(poke_info[NAME], int(poke_info[HP]), int(poke_info[ATK]), int(poke_info[DEFE]),
                                      int(poke_info[SPEED]),
                                      [poke_info[TYPE1], poke_info[TYPE2]])
                    pokemon.id = poke_id
                    self.pokeList.append(pokemon)
                    poke_id += 1
                else:
                    firstLineIgnored = True

        if not all_poke_info:
            raise LoadError(f"Cannot read file '{filename}'")

        #teamA é o time de uma instancia do problema
        for i in range(3):
            self.teamA.append(self.pokeList[i])
        # CONSTRUIR OS 1000 TIMES

    def readChartFile(self):
        with open('chart.csv', newline='') as chartFile:
            chartInfo = csv.reader(chartFile)
            # for chartRow in chartInfo:
            #     print(chartRow)

    # only attacking(cp2) pokemon is modified by multiplier
    def battle(self, teamB) -> float:
        battleResult = 0.0
        for pokeA in self.teamA:
            for pokeB in teamB:
                battleResult += pokeB.calculateCP() - pokeA.calculateCP()
        return battleResult
