from transport.Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, color, capacity):
        super().__init__(capacity)
        self.color = color
       