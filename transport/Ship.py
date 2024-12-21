from transport.Vehicle import Vehicle


class Ship(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(capacity)
        self.name = name
    