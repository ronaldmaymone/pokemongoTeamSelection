import numpy as np
from brkga_mp_ipr.types import BaseChromosome, BrkgaParams
from brkga_mp_ipr.algorithm import BrkgaMpIpr
from brkga_mp_ipr.enums import Sense
from brkga_mp_ipr.types_io import load_configuration
import csv
import random
import time

from poke_decoder import PokeDecoder
from poke_instance import PokeInstance
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
configuration_file = 'config.conf'
seed = 2
chromosome_size = 3
num_generations = 300

#pokeList = list()
#firstLineIgnored = False


def runBRKGA():

    print("Reading data...")
    instance = PokeInstance('pokemon.csv')

    print("Reading parameters...")
    brkga_params, _ = load_configuration(configuration_file)

    print("Building BRKGA data and initializing...")
    decoder = PokeDecoder(instance)

    brkga = BrkgaMpIpr(
        decoder=decoder,
        sense=Sense.MAXIMIZE,
        seed=seed,
        chromosome_size=chromosome_size,
        params=brkga_params
    )

    start = time.perf_counter()
    # NOTE: don't forget to initialize the algorithm.
    brkga.initialize()

    ########################################
    # Find good solutions / evolve
    ########################################

    print(f"Evolving {num_generations} generations...")
    brkga.evolve(num_generations)

    best_cost = brkga.get_best_fitness()
    end = time.perf_counter()
    print(f"Best cost: {best_cost}")
    print(f"Time elapsed: {end - start:0.4f}")


# def readPokemonFile():
#
#     with open('pokemon.csv', newline='') as pokemonFile:
#         firstLineIgnored = False
#         pokeInfo = csv.reader(pokemonFile)
#         for poke in pokeInfo:
#             #Lista com todas as infos do pokemon
#             if(firstLineIgnored):
#                 pokeList.append(Pokemon(poke[NAME], int(poke[HP]), int(poke[ATK]), int(poke[DEFE]), int(poke[SPEED]), [poke[TYPE1], poke[TYPE2]]))
#             else:
#                 firstLineIgnored = True


def readChartFile():
    with open('chart.csv', newline='') as chartFile:
        chartInfo = csv.reader(chartFile)
        for chartRow in chartInfo:
            print(chartRow)
