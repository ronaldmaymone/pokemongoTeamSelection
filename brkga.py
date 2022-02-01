from brkga_mp_ipr.algorithm import BrkgaMpIpr
from brkga_mp_ipr.enums import Sense
from brkga_mp_ipr.types_io import load_configuration
import csv
import time
from poke_decoder import PokeDecoder
from poke_instance import PokeInstance

configuration_file = 'config.conf'
seed = 22
chromosome_size = 3
num_generations = 20


def runBRKGA() -> (float, float):

    #print("Reading data...")
    instance = PokeInstance('pokemon.csv')

    #print("Reading parameters...")
    brkga_params, _ = load_configuration(configuration_file)

    #print("Building BRKGA data and initializing...")
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

    #print(f"Evolving {num_generations} generations...")
    brkga.evolve(num_generations)

    best_cost = brkga.get_best_fitness()
    end = time.perf_counter()
    #print(f"Best cost: {best_cost}")
    #print(f"Time elapsed: {end - start:0.4f}")
    return round(best_cost, 4), round(end - start, 4)

