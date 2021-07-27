from jirachi_core.gen1_text import Gen1Text
from jirachi_core.item import Item
from jirachi_core.pokedex_entry import PokedexEntry
from jirachi_core.pokemon_save import PokemonSave
from jirachi_core.utils import Utils

class Gen1Save(PokemonSave):
    text_encoder = Gen1Text()

    def get_box_pokemon(self, box_no):
        return

    def get_casino_coins(self):
        return Utils.read_bytes_to_decimal(self.bytes[0x2850:0x2852], bcd=True)

    def get_inventory_items(self):
        item_count = self.bytes[0x25C9]
        items = []

        for i in range(0, item_count):
            byte_index = 0x25C9 + (2*i) + 1
            item_id, item_amount = self.bytes[byte_index:byte_index+2]
            if item_id == 0xFF:
                break
            items.append(Item(item_id, item_amount))
        
        return items

    def get_party_pokemon(self):
        return
    
    def get_play_time(self):
        return (self.bytes[0x2CED], self.bytes[0x2CEF], self.bytes[0x2CF0])

    def get_player_name(self):
        return self.text_encoder.bytes_to_char_array(self.bytes[0x2598:0x25A4])
    
    def get_pokedex(self):
        seen_bytes = self.bytes[0x25B6:0x25C9]
        caught_bytes = self.bytes[0x25A3:0x25B6]
        return [PokedexEntry(i+1, bool(seen_bytes[i >> 3] >> (i & 7) & 1), bool(caught_bytes[i >> 3] >> (i & 7) & 1)) for i in range(0, 151)]

    def get_pokedollars(self):
        return Utils.read_bytes_to_decimal(self.bytes[0x25F3:0x25F6], bcd=True)
    
    def get_trainer_id(self):
        return Utils.read_bytes_to_decimal(self.bytes[0x2605:0x2607])