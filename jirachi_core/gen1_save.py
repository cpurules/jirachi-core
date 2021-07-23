from jirachi_core.pokemon_save import PokemonSave
from jirachi_core.utils import Utils

class Gen1Save(PokemonSave):
    def get_box_pokemon(self, box_no):
        return

    def get_casino_coins(self):
        return Utils.bcd_to_decimal(self.bytes[0x2850:0x2852])

    def get_party_pokemon(self):
        return

    def get_player_name(self):
        return

    def get_pokedollars(self):
        return