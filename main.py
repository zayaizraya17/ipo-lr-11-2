from transport.Client import Client
from transport.Vehicle import Vehicle
from transport.Ship import Ship
from transport.Truck import Truck
from transport.TransportCompany import TransportCompany

def main():
    
    company = TransportCompany("Компания")

    while True:
        print('''1. Добавить клиента
2. Добавить транспортное средство
3. Показать транспортные средства
4. Оптимизировать распределение грузов
5. Показать клиентов"
6. Выйти''') 

        choice = input("Выберите действие: ")

        if choice == '1':
            while True:
                name = input("Введите имя клиента: ")
                if name != "":
                    break
                else:
                    print("Введите данные")

            while True:
                try: 
                    cargo_weight = float(input("Введите вес груза: "))
                    break 
                except ValueError:
                    print("Некорректные данные")

            while True:
                is_vip = input("Введите VIP клиент? (yes/no): ")
                if is_vip.lower() in ["yes", "no"]:
                    is_vip = is_vip.lower() == "yes"
                    break
                else:
                    print("Некорректные данные")


            client = Client(name, cargo_weight, is_vip)
            company.add_client(client)
    
        elif choice == '2':

            while True:
                vtype = input("Тип транспорта (ship/truck): ")
                if vtype.lower() in ["ship", "truck"]:
                    vtype = vtype
                    break
                else:
                    print("Некорректные данные")

            while True:
                try: 
                    capacity = float(input("Введите грузоподъемность: "))
                    break 
                except ValueError:
                    print("Некорректные данные")


            if vtype == 'ship':

                while True:
                    name = input("Введите название судна: ")
                    if name != "":
                        break
                    else:
                        print("Введите данные")
                        
                vehicle = Ship(name, capacity)

            elif vtype == 'truck':
                while True:
                    color = input("Введите цвет грузовика: ")
                    if color != "":
                        break
                    else:
                        print("Введите данные")
                
                vehicle = Truck(color, capacity)
            else:
                print("Неверный тип транспорта")
                continue

            company.add_vehicle(vehicle)
        

        elif choice == '3':
            for transport in company.list_vehicles():
                print(transport)
        
        elif choice == '4':
            company.optimize_cargo_distribution()
            for vehicle in company.list_vehicles():
                print(vehicle)
                for client in vehicle.clients_list:
                    print(f"  Клиент: {client.name}, Вес груза: {client.cargo_weight}, VIP: {client.is_vip}")
        
        elif choice == '5': 
            vip_clients, regular_clients = company.list_clients() 
            print("VIP клиенты:") 
            for client in vip_clients: 
                print(f" Клиент: {client.name}, Вес груза: {client.cargo_weight}") 
                print("Не VIP клиенты:") 
                for client in regular_clients: 
                    print(f" Клиент: {client.name}, Вес груза: {client.cargo_weight}")

        elif choice == '6':
            break


main()