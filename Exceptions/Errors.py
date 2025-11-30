class DuplicateQrIDError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class InvalidCPF(Exception):
    def __init__(self, *args):
        super().__init__(*args)