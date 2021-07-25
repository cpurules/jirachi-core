from abc import ABC, abstractmethod

class PokemonSave(ABC):
    def __init__(self, bytes):
        self.bytes = bytes
        super().__init__()
    
    @abstractmethod
    def get_box_pokemon(self, box_no):
        pass

    @abstractmethod
    def get_casino_coins(self):
        pass

    @abstractmethod
    def get_inventory_items(self):
        pass

    @abstractmethod
    def get_party_pokemon(self):
        pass

    @abstractmethod
    def get_play_time(self):
        pass

    @abstractmethod
    def get_player_name(self):
        pass

    @abstractmethod
    def get_pokedollars(self):
        pass

    @abstractmethod
    def get_trainer_id(self):
        pass