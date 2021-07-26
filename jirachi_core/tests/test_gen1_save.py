import pytest
import os

from jirachi_core.gen1_save import Gen1Save
from jirachi_core.pokedex_entry import PokedexEntry
from jirachi_core.utils import Utils

@pytest.fixture
def blue_save_1():
    return Gen1Save(Utils.read_bytes('tests/saves/blue_1.dat'))

class TestGen1Save:
    def test_get_casino_coins(self, blue_save_1):
        assert blue_save_1.get_casino_coins() == 3455
    
    def test_get_play_time(self, blue_save_1):
        assert blue_save_1.get_play_time() == (31, 35, 5)

    def test_get_player_name(self, blue_save_1):
        assert blue_save_1.get_player_name() == ['R', 'e', 'g', 'n', 'u', 'm']

    def test_get_pokedex(self, blue_save_1):
        pokedex = blue_save_1.get_pokedex()
        assert (pokedex[0] == PokedexEntry(1, True, False) and
                pokedex[2] == PokedexEntry(3, False, False) and
                pokedex[6] == PokedexEntry(7, True, True))

    def test_get_pokedollars(self, blue_save_1):
        assert blue_save_1.get_pokedollars() == 20379
    
    def test_get_trainer_id(self, blue_save_1):
        assert blue_save_1.get_trainer_id() == 14494