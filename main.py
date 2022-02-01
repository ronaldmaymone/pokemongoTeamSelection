import brkga
import statistics
import numpy as np
from operator import itemgetter
if __name__ == '__main__':
    # quantidade de instancias do problema. Cada instancia encontrar o melhor time B para enfrentar um dado time A fixo.
    total_instance_number = 100
    current_instance = 1
    solutions = []
    timings = []

    while current_instance <= total_instance_number:
        best_fitness, time = brkga.runBRKGA()
        print(f"Fitness: {best_fitness}. Time elapsed: {time}")
        solutions.append(best_fitness)
        timings.append(time)
        current_instance += 1

    with open('output.txt', 'w') as outputFile:
        outputFile.write(f"Fitness Mean: {round(statistics.mean(solutions), 4)}. Fitness Std Deviation: {round(statistics.stdev(solutions), 4)}\n")
        outputFile.write(f"Time mean: {round(statistics.mean(timings), 4)}. Time Std Deviation: {round(statistics.stdev(timings), 4)}")
