from math import floor

from brkga_mp_ipr.types import BaseChromosome

from poke_instance import PokeInstance


class PokeDecoder():

    def __init__(self, instance: PokeInstance):
        self.instance = instance

    def decode(self, chromosome: BaseChromosome, rewrite: bool) -> float:
        # print(len(self.instance.pokeList))
        teamB = []
        # procurar na lista de pokemon cada gene.
        for gene in chromosome:
            teamB.append(self.instance.pokeList[self.findPokeListIndex(gene)])
        return self.instance.battle(teamB)

    @staticmethod
    def findPokeListIndex(gene: float) -> int:
       # print(round(gene, 4))
       # print("Then the int is...")
       # print(round(801 * round(gene, 4)))
        return round(799 * round(gene, 4))
