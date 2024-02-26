from typing import List
from python_oop.first_steps_in_oop_lecture.project import Pokemon

class Trainer:

    def __init__(self, name: str):
        self.pokemons: List[Pokemon] = []
        self.name = name

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if not pokemon in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()} with health {pokemon_health}"
        return "This pokemon is already caught"


    def release_pokemon(self, pokemon_name: string):
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"

    def trainer_data(self):
        f""" 
    Pokemon Trainer {self.name}
    Pokemon count {len(self.pokemons)}
        """
