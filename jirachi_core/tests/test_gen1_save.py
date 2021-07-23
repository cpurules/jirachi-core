import pytest
import os

from jirachi_core.gen1_save import Gen1Save
from jirachi_core.utils import Utils

@pytest.fixture
def blue_save_1():
    return Gen1Save(Utils.read_bytes('tests/saves/blue_1.dat'))

class TestGen1Save:
    def test_get_casino_coins(self, blue_save_1):
        assert blue_save_1.get_casino_coins() == 3455
    
    def test_get_pokedollars(self, blue_save_1):
        assert blue_save_1.get_pokedollars() == 20379
    
    def test_get_trainer_id(self, blue_save_1):
        assert blue_save_1.get_trainer_id() == 14494