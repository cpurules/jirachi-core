class Utils:
    @staticmethod
    def read_bytes(path):
        file_bytes = None
        with open(path) as f:
            file_bytes = f.read()
        return file_bytes