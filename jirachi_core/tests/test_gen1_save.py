from jirachi_core.gen1_save import Gen1Save
from jirachi_core.utils import Utils

class TestGen1Save:
    def __init__(self):
        self.blue_save_1 = Gen1Save(Utils.read_bytes('saves/blue_1.dat'))