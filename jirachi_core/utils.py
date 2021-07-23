class Utils:
    @staticmethod
    def read_bytes(path):
        bytes = None
        with open(path) as f:
            bytes = f.read()
        return bytes