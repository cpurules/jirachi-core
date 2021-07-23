class Utils:
    @staticmethod
    def read_bytes(path):
        file_bytes = None
        with open(path, 'rb') as f:
            file_bytes = f.read()
        return file_bytes
    
    @staticmethod
    def read_bytes_to_decimal(bts, bcd=False):
        dec = 0
        power = len(bts) - 1

        for b in bts:
            if bcd:
                dec = dec + int(hex(b)[2:]) * pow(10, power * 2)
            else:
                dec = dec + b * pow(256, power)
            
            power = power - 1
        
        return dec