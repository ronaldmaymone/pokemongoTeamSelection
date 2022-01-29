import numpy as np
from brkga_mp_ipr.types import BaseChromosome
from pymoo.algorithms.soo.nonconvex.brkga import BRKGA
from pymoo.optimize import minimize
import csv
import random
from pokemon import Pokemon

NAME = 1
TYPE1 = 2
TYPE2 = 3
HP = 5
ATK = 6
DEFE = 7
SPEED = 10
teamA = []
teamB = []

class Problem:
    def __init__(self):
        pass


pokeList = list()
#firstLineIgnored = False


def runBRKGA():
    for i in range(3):
        teamA.append(pokeList[random.randint(0, len(pokeList))])
        teamB.append(pokeList[random.randint(0, len(pokeList))])
    for i, _poke in enumerate(teamA):
        print(_poke.name+" vs "+teamB[i].name)
    # algorithm = BRKGA(
    #     n_elites=200,
    #     n_offsprings=700,
    #     n_mutants=100,
    #     bias=0.7)
    #
    # res = minimize(problem,
    #                algorithm,
    #                ("n_gen", 75),
    #                seed=1,
    #                verbose=False)
    # return res

def readPokemonFile():

    with open('pokemon.csv', newline='') as pokemonFile:
        firstLineIgnored = False
        pokeInfo = csv.reader(pokemonFile)
        for poke in pokeInfo:
            #Lista com todas as infos do pokemon
            if(firstLineIgnored):
                pokeList.append(Pokemon(poke[NAME], int(poke[HP]), int(poke[ATK]), int(poke[DEFE]), int(poke[SPEED]), [poke[TYPE1], poke[TYPE2]]))
            else:
                firstLineIgnored = True
        #print(pokeList[2].types + pokeList[3].types)

def readChartFile():
    with open('chart.csv', newline='') as chartFile:
        chartInfo = csv.reader(chartFile)
        # for chartRow in chartInfo:
        #     print(chartRow)

#only attacking(cp2) pokemon is modified by multiplier
def battle(cp1, cp2):
    battleResult = 0.0
    for pokeA in teamA:
        for pokeB in teamB:
            battleResult += pokeB.calculateCP() - pokeA.calculateCP()
    return battleResult

#dado um timeA, qual melhor time para enfrenta-lo
#uma solucao do problema é o resultado de uma batalha(CP resultante)
def decode(self, chromosome: BaseChromosome, rewrite: bool) -> float:
    #construir lista de listas com cromossomo(random key) e pokemon(talvez cp dele)
    # retornar como fitness o resultado da batalha
    #CP after battle
    pass