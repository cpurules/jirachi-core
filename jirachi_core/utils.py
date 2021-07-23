class Utils:
    @staticmethod
    def read_bytes(path):
        file_bytes = None
        with open(path, 'rb') as f:
            file_bytes = f.read()
        return file_bytes
    
    @staticmethod
    def bcd_to_decimal(bcd_bytes):
        dec = 0
        power = len(bcd_bytes) - 1
        for b in bcd_bytes:
            dec = dec + (int(hex(b)[2:]) * pow(10, power * 2))
            power = power - 1
        return dec