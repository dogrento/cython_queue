class Fila():
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True

        return False

    def append_to_fila(self, item):
        # self.data = item
        self.data.append(item)
