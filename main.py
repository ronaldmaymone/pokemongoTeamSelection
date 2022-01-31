import brkga
from operator import itemgetter
if __name__ == '__main__':
    # quantidade de instancias do problema. Cada instancia encontrar o melhor time B para enfrentar um dado time A fixo.
    total_instance_number = 10
    current_instance = 1

    while current_instance <= total_instance_number:
        brkga.runBRKGA()
        current_instance += 1
