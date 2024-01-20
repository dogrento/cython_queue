class Fila():
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True

        return False

    def append_to_fila(self, item):
        self.data.append(item)

    def pop_from_fila(self):
        if self.is_empty():
            raise IndexError("Fila is Empty.")

        self.data.pop(0)
