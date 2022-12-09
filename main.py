import random


class Human:

    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):  # Когда запрашиваем значение пишем get
        self.home = Home()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return

        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return

        self.money += self.job.salary
        self.gladness += self.job.gladness_less

    def shopping(self):
        pass

    def chill(self):
        self.home.mess += 5
        self.gladness += 5
        self.money -= 5
        self.satiety += 5

    def clear_home(self):
        self.home.mess = 0
        self.gladness -= 5
        self.money -= 5
        self.satiety -= 5

    def to_repair(self):
        self.car.strength = 100
        self.money -= 10
        self.gladness += 5

    def indexes_day(self, day):
        pass

    def is_alive(self):
        if self.gladness <= 0:
            print('You are depressed!')
            return False
        if self.money <= 0:
            print('You are bankrupt!')
            return False
        if self.satiety <= 0:
            print('You are very hungry!')
            return False

    def live(self):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move...')
            return False


class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 15},  # Словарь и ключи
                'Lada': {'fuel': 70, 'strength': 20, 'consumption': 8},
                'Volvo': {'fuel': 150, 'strength': 100, 'consumption': 10},
                'Ford': {'fuel': 120, 'strength': 80, 'consumption': 12}}

print(brand_of_car.keys())
print(list(brand_of_car))

job_list = {'Java': {'salary': 50, 'gladness_less': 10},
            'C++': {'salary': 80, 'gladness_less': 5},
            'Python': {'salary': 30, 'gladness_less': 8},
            'Rust': {'salary': 60, 'gladness_less': 6}}
