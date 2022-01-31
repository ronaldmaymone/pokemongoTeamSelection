import math
C = 0.7903
Aiv, Div, Siv = 15, 15, 15


class Pokemon:
    def __init__(self, _name, _hp, _atk, _def, _stam, _types):
        self.id = 0
        self.name = _name
        self.hp = _hp
        self.atk = _atk
        self.def_ = _def
        self.stam = _stam
        self.types = _types
        self.cp = self.calculateCP()

    """Calcula o CP do Pokémon"""
    def calculateCP(self) -> float:
        return ((self.atk + Aiv) * (math.sqrt(self.def_ + Div)) * (math.sqrt(self.stam + Siv)) * math.pow(C, 2)) / 10


# class Team:
#     def __init__(self):
#         self.id = 0
#         self
