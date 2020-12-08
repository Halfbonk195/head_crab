# -*- coding: utf-8 -*-
from pprint import pprint
from random import randint
from termcolor import cprint


# Реализуем модель доставки грузов

# Дорога - хранит расстояния между обьектами
# Склад - хранит груз и управляет очередями грузовиков

# Базовый класс - Машина,
# имеет
#   кол-во топлива
# может
#   заправляться

# Грузовик (производный от Машина)
# имеет
#   емкость кузова, скорость движения, расход топлива за час поездки
# может
#   стоят под погрузкой/разгрузкой
#   ехать со скоростью

# Погрузчик (производный от Машина)
# имеет
#   скорость погрузки, расход топлива в час при работе
# может
#   загружать/разгружать грузовик
#   ждать грузовик


class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:

    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return 'Склад {}, груза {}'.format(self.name, self.content)

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.reverse()
        self.queue_in.append(truck)
        self.queue_in.reverse()
        truck.place = self
        # print('{} прибыл грузовик {} '.format(self.name, truck))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        # print('{} грузовик готов {} '.format(self.name, truck))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{} топлива {}'.format(self.model, self.fuel)

    def tank_up(self):
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        # print('{} заправился'.format(self.model))

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
            return False
        return True


class Truck(Vehicle):
    fuel_rate = 50
    dead_time = 0

    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + ', груза {}'.format(self.cargo)

    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target >= self.velocity:
            self.distance_to_target -= self.velocity
            # print('{} с грузом {}, едет по дороге из {} в {}, осталось {}'.format(
            #     self.model, self.cargo, self.place.start, self.place.end, self.distance_to_target))
        else:
            self.place.end.truck_arrived(truck=self)
            # print('{} доехал '.format(self.model))

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        # print('{} выехал в путь из {} до {}'.format(self.model, self.place.start, self.place.end))

    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.dead_time += 1


class OtherTruck(Truck):
    fuel_rate = 100


class AutoLoader(Vehicle):
    fuel_rate = 30
    dead_time = 0

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + ' грузим {}'.format(self.truck)

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.warehouse.get_next_truck()
                if self.truck is None:
                    # print('{} нет грузовиков для работы'.format(self.model))
                    AutoLoader.dead_time += 1
                # else:
                #     print('{} взял в работу {}'.format(self.model, self.truck))
            elif self.role == 'loader':
                self.load()
            else:
                self.unload()

    def load(self):
        if self.warehouse.content == 0:
            # print('{} на складе ничего нет!'.format(self.model))
            if self.truck:
                self.warehouse.truck_ready(self.truck)
                self.truck = None
            return
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            cargo = self.bucket_capacity
        else:
            cargo = truck_cargo_rest
        if self.warehouse.content < cargo:
            cargo = self.warehouse.content
        self.warehouse.content -= cargo
        self.truck.cargo += cargo
        # print('{} грузил {}'.format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.warehouse.content += self.truck.cargo
            self.truck.cargo = 0
        # print('{} разгружал {}'.format(self.model, self.truck))
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None


def recycle(loaders_number, unloaders_number, truck_1_number, truck_2_number):
    TOTAL_CARGO = 100000
    result = []

    moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
    piter = Warehouse(name='Питер', content=0)

    moscow_piter = Road(start=moscow, end=piter, distance=715)
    piter_moscow = Road(start=piter, end=moscow, distance=780)

    moscow.set_road_out(moscow_piter)
    piter.set_road_out(piter_moscow)

    loaders = []
    for number in range(loaders_number):
        loader = AutoLoader(model='Bobcat №{}'.format(number + 1), bucket_capacity=1000, warehouse=moscow,
                            role='loader')
        loaders.append(loader)
    unloaders = []
    for number in range(unloaders_number):
        unloader = AutoLoader(model='Lonking №{}'.format(number + 1), bucket_capacity=500, warehouse=piter,
                              role='unloader')
        unloaders.append(unloader)

    trucks = []
    for number in range(truck_1_number):
        truck = Truck(model='КАМАЗ №{}'.format(number + 1), body_space=5000)
        moscow.truck_arrived(truck)
        trucks.append(truck)
    for number in range(truck_2_number):
        truck = OtherTruck(model='Volvo №{}'.format(number + 1), body_space=10000)
        moscow.truck_arrived(truck)
        trucks.append(truck)

    hour = 0
    while piter.content < TOTAL_CARGO:
        hour += 1
        # cprint('---------------- Час {} ---------------'.format(hour), color='red')
        for truck in trucks:
            truck.act()
        for loader in loaders:
            loader.act()
        for unloader in unloaders:
            unloader.act()
        moscow.act()
        piter.act()
    #     for truck in trucks:
    #         cprint(truck, color='cyan')
    #     for loader in loaders:
    #         cprint(loader, color='cyan')
    #     for unloader in unloaders:
    #         cprint(unloader, color='cyan')
    #     cprint(moscow, color='cyan')
    #     cprint(piter, color='cyan')
    #
    # cprint('Всего затрачено топлива {}'.format(Vehicle.total_fuel), color='yellow')
    # cprint('Общий простой грузовиков {}'.format(Truck.dead_time), color='yellow')
    # cprint('Общий простой погрузчиков {}'.format(AutoLoader.dead_time), color='yellow')
    result.append(Vehicle.total_fuel)
    result.append(Truck.dead_time)
    result.append(AutoLoader.dead_time)
    result.append(hour)
    return result


result_dict = dict()
for loaders_number in range(1, 10):
    for unloaders_number in range(1, 10):
        for truck_1_number in range(1, 10):
            for truck_2_number in range(1, 10):
                if loaders_number < 5 and (truck_1_number + truck_2_number) > 5:
                    continue
                if loaders_number < 7 and (truck_1_number + truck_2_number) > 7:
                    continue
                if unloaders_number < 5 and (truck_1_number + truck_2_number) > 5:
                    continue
                if unloaders_number < 7 and (truck_1_number + truck_2_number) > 7:
                    continue
                if (truck_1_number + truck_2_number) < 5 and loaders_number > 5:
                    continue
                if (truck_1_number + truck_2_number) < 5 and unloaders_number > 5:
                    continue
                if (truck_1_number + truck_2_number) < 7 and loaders_number > 6:
                    continue
                if (truck_1_number + truck_2_number) < 7 and unloaders_number > 6:
                    continue
                key = 'Количество: погрузчиков - {}, разгрузчиков - {}, Камазов' \
                      ' - {}, Volvo - {}'.format(loaders_number, unloaders_number, truck_1_number, truck_2_number)
                result_dict[key] = recycle(loaders_number=loaders_number, unloaders_number=unloaders_number,
                                           truck_1_number=truck_1_number, truck_2_number=truck_2_number)
                sum_for_dead_time = (result_dict[key][0] + result_dict[key][1]) * 10
                sum_for_fuel = result_dict[key][2] * 40
                sum_for_hours = (loaders_number + unloaders_number + truck_1_number + truck_2_number) * \
                                result_dict[key][3] * 200
                sum_all = sum_for_fuel + sum_for_dead_time + sum_for_hours
                result_dict[key].append(sum_for_dead_time)
                result_dict[key].append(sum_for_fuel)
                result_dict[key].append(sum_for_hours)
                result_dict[key].append(sum_all)
            # print(key)

compare_sum = 1e10
min_sum = None
min_key = None
for key in result_dict:
    print(key, result_dict[key])
    current_sum = result_dict[key][7]
    if current_sum > compare_sum:
        min_sum = compare_sum
    else:
        compare_sum = current_sum
        min_key = key
print()
print(min_key, '\nТопливо', result_dict[min_key][0], 'Простой грузовиков', result_dict[min_key][1], 'Простой погрузчиков',
      result_dict[min_key][2], 'Всего времени', result_dict[min_key][3], 'Стоимость простоя', result_dict[min_key][4],
      'Стоимость топлива', result_dict[min_key][5], 'Стоимость часов', result_dict[min_key][6], 'Общая стоимость',
      result_dict[min_key][7])
print(min_sum)


compare_sum = 1e10
min_sum = None
min_key = None
for key in result_dict:
    current_sum = result_dict[key][3]
    if current_sum > compare_sum:
        min_sum = compare_sum
    else:
        compare_sum = current_sum
        min_key = key
print()
print(min_key, '\nТопливо', result_dict[min_key][0], 'Простой грузовиков', result_dict[min_key][1], 'Простой погрузчиков',
      result_dict[min_key][2], 'Всего времени', result_dict[min_key][3], 'Стоимость простоя', result_dict[min_key][4],
      'Стоимость топлива', result_dict[min_key][5], 'Стоимость часов', result_dict[min_key][6], 'Общая стоимость',
      result_dict[min_key][7])
print(min_sum)


compare_sum = 1e10
min_sum = None
min_key = None
for key in result_dict:
    current_sum = result_dict[key][2]
    if current_sum > compare_sum:
        min_sum = compare_sum
    else:
        compare_sum = current_sum
        min_key = key
print()
print(min_key, '\nТопливо', result_dict[min_key][0], 'Простой грузовиков', result_dict[min_key][1], 'Простой погрузчиков',
      result_dict[min_key][2], 'Всего времени', result_dict[min_key][3], 'Стоимость простоя', result_dict[min_key][4],
      'Стоимость топлива', result_dict[min_key][5], 'Стоимость часов', result_dict[min_key][6], 'Общая стоимость',
      result_dict[min_key][7])
print(min_sum)

compare_sum = 1e10
min_sum = None
min_key = None
for key in result_dict:
    current_sum = result_dict[key][0]
    if current_sum > compare_sum:
        min_sum = compare_sum
    else:
        compare_sum = current_sum
        min_key = key
print()
print(min_key, '\nТопливо', result_dict[min_key][0], 'Простой грузовиков', result_dict[min_key][1], 'Простой погрузчиков',
      result_dict[min_key][2], 'Всего времени', result_dict[min_key][3], 'Стоимость простоя', result_dict[min_key][4],
      'Стоимость топлива', result_dict[min_key][5], 'Стоимость часов', result_dict[min_key][6], 'Общая стоимость',
      result_dict[min_key][7])
print(min_sum)