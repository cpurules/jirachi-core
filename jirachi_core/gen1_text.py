from jirachi_core.utils import Utils

class Gen1Text():
    def __init__(self):
        self.character_map = {}

        # A - Z = 0x80 - 0x99
        for i in range(0x80, 0x99 + 1):
            self.character_map[i] = chr(ord('A') + i - 0x80)
        
        # Some punctuation
        self.character_map[0x9A] = '('
        self.character_map[0x9B] = ')'
        self.character_map[0x9C] = ':'
        self.character_map[0x9D] = ';'
        self.character_map[0x9E] = '['
        self.character_map[0x9F] = ']'

        # a - z = 0xA0 - 0xB9
        for i in range(0xA0, 0xB9 + 1):
            self.character_map[i] = chr(ord('a') + i - 0xA0)
        
        # Some special characters
        self.character_map[0xBA] = 'é'
        self.character_map[0xBB] = '\'d'
        self.character_map[0xBC] = '\'l'
        self.character_map[0xBD] = '\'s'
        self.character_map[0xBE] = '\'t'
        self.character_map[0xBF] = '\'v '

        # Additional special chars
        self.character_map[0xE0] = '\''
        self.character_map[0xE1] = 'PK'
        self.character_map[0xE2] = 'MN'
        self.character_map[0xE3] = '-'
        self.character_map[0xE4] = '\'r'
        self.character_map[0xE5] = '\'m'
        self.character_map[0xE6] = '?'
        self.character_map[0xE7] = '!'
        self.character_map[0xE8] = '.'
        self.character_map[0xEC] = '\N{BLACK DOWN-POINTING TRIANGLE}'
        self.character_map[0xED] = '\N{BLACK RIGHT-POINTING SMALL TRIANGLE}'
        self.character_map[0xEE] = '\N{WHITE RIGHT-POINTING SMALL TRIANGLE}'
        self.character_map[0xEF] = '\N{MALE SIGN}'
        self.character_map[0xF0] = 'P$'
        self.character_map[0xF1] = '\N{MULTIPLICATION SIGN}'
        self.character_map[0xF2] = '.'
        self.character_map[0xF3] = '/'
        self.character_map[0xF4] = ','
        self.character_map[0xF5] = '\N{FEMALE SIGN}'
        
        # 0 - 9 = 0xF6 - 0xFF
        for i in range(0xF6, 0xFF + 1):
            self.character_map[i] = str(i - 0xF6)
        
        self.inv_character_map = {v: k for k, v in self.character_map.items()}
    
    def char_array_to_bytes(self, chars):
        return_bytes = []
        for c in chars:
            return_bytes.append(self.inv_character_map[c])
        return return_bytes
    
    def bytes_to_char_array(self, bytes):
        return_chars = []
        for b in bytes:
            if b == 0x50:
                break
            return_chars.append(self.character_map[b])
        return return_chars