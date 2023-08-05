class Race():
  def __init__(self, name, driver_limit, drivers):
    self.name = name
    self.driver_limit = driver_limit
    self.drivers = drivers
    print(f'Race Info:\n\tRace Name: {self.name}\n\tDriver Limit: {self.driver_limit}\n\tDrivers: {self.drivers}')

class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

myCar.talk('Michael')

race = Race("Indy 500", 3, ["Bill", "Jim", "John"])