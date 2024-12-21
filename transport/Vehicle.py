import uuid
from transport.Client import Client


class Vehicle():
    def __init__(self, capacity):
        self.vehicle_id = str(uuid.uuid4())[:8]
        self.capacity = capacity
        self.current_load = 0
        self.clients_list = []
    
    def load_cargo(self, client):
        if self.current_load + client.cargo_weight > self.capacity:
            print("Слишком тяжело")
            return
        self.current_load += client.cargo_weight 
        self.clients_list.append(client)

    def __str__(self):
        return f"ID транспорта: {self.vehicle_id} Грузоподъемность: {self.capacity}, Текущая загрузка: {self.current_load}"