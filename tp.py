class Pokemon:
    def __init__(self, number, name, types, level):
        self.number = number
        self.name = name
        self.types = types
        self.level = level

    def __repr__(self):
        return f"{self.name}(#{self.number}, Lv.{self.level}, Types: {', '.join(self.types)})"

class Pokedex:
    def __init__(self):
        self.type_hash = {}
        self.last_digit_hash = {}
        self.level_hash = [[] for _ in range(10)]

    def add_pokemon(self, pokemon):

        for pokemon_type in pokemon.types:
            if pokemon_type not in self.type_hash:
                self.type_hash[pokemon_type] = []
            self.type_hash[pokemon_type].append(pokemon)


        last_digit = pokemon.number % 10
        if last_digit not in self.last_digit_hash:
            self.last_digit_hash[last_digit] = []
        self.last_digit_hash[last_digit].append(pokemon)


        level_index = pokemon.level % 10
        self.level_hash[level_index].append(pokemon)

    def get_pokemons_by_last_digit(self, digits):
        result = []
        for digit in digits:
            result.extend(self.last_digit_hash.get(digit, []))
        return result

    def get_pokemons_by_level_multiple(self, multiples):
        result = []
        for multiple in multiples:
            for level_index in range(10):
                if level_index % multiple == 0:
                    result.extend(self.level_hash[level_index])
        return result

    def get_pokemons_by_types(self, types):
        result = []
        for pokemon_type in types:
            result.extend(self.type_hash.get(pokemon_type, []))
        return result


pokedex = Pokedex()


pokedex.add_pokemon(Pokemon(25, "Pikachu", ["Electrico"], 50))
pokedex.add_pokemon(Pokemon(6, "Charizard", ["Fuego", "Volador"], 36))
pokedex.add_pokemon(Pokemon(147, "Dratini", ["Dragon"], 30))
pokedex.add_pokemon(Pokemon(208, "Steelix", ["Acero", "Tierra"], 45))

print("")
print("Pokémons cuyos números terminan en 3, 7 y 9:")
print(pokedex.get_pokemons_by_last_digit([3, 7, 9]))


print("")
print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
print(pokedex.get_pokemons_by_level_multiple([2, 5, 10]))

print("")
print("\nPokémons de los tipos Acero, Fuego, Electrico, Hielo:")
print(pokedex.get_pokemons_by_types(["Acero", "Fuego", "Electrico", "Hielo"]))
