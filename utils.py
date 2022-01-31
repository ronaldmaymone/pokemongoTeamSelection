def pickTypeListPos(typeString: str) -> int:
    switcher = {
        "Normal": 1,
        "Fire": 2,
        "Water": 3,
        "Electric": 4,
        "Grass": 5,
        "Ice": 6,
        "Fighting": 7,
        "Poison": 8,
        "Ground": 9,
        "Flying": 10,
        "Psychic": 11,
        "Bug": 12,
        "Rock": 13,
        "Ghost": 14,
        "Dragon": 15,
        "Dark": 16,
        "Steel": 17,
        "Fairy": 18
    }
    return switcher.get(typeString, "Invalid type")
