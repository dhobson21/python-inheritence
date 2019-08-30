#Custom Colors and Sounds

#Define 5 of your favorite vehicles
#Move all common properties in your vehicles to a new Vehicle class.

class Vehicle:

  def __init__(self, make, model, year, color):
    self.make =  make
    self.model = model
    self.year = year
    self.main_color = color

  #Create a drive() method in the Vehicle class.
  def drive (self):
    print(f'The {self.main_color} {self.model} drives past. RRrrrrrummbbble!')

  def turn (self, direction):
    print(f'The {self.make} {self.model} turned {direction}')

  def stop (self):
    print(f'The {self.make} {self.model} hit the brakes. SCREECHHHHHHHHH')

class SUV(Vehicle):

  def __init__(self):
    self.hatch = True
    self.heat_seats = True

  def drive (self):
    print(f'The {self.main_color} {self.model} drives past. Brrrrrrrrruuuuggggg!')



class Truck(Vehicle):

  def __init__(self):
    self.truck_bed = True
    self.can_tow = True
    self.green = False

  def drive (self):
    print(f'The {self.main_color} {self.model} drives past. RRrrrrrummbbble!!')

  def stop (self):
    print(f'The {self.make} {self.model} came to a long, slow stop')


class Sedan(Vehicle):

  def __init__(self):
    self.doors = 4
    self.seats = 5

  def drive (self):
    print(f'The {self.main_color} {self.model} drives past VVRrooommmmm!!')

class Coup(Vehicle):

  def __init__(self):
    self.doors =2
    self.transmission = "Manual"

  def drive (self):
    print(f'The {self.main_color} {self.model} drives past. Grrrrrrrrrrrrr!!')

  def stop (self):
    print(f'The {self.make} {self.model} hit the brakes and stopped rather quickly')

class Sports_car(Vehicle):

  def __init__(self):
    self.seats = 2
    self.gas = "bad"

  def drive (self):
    print(f'The {self.main_color} {self.model} drives past PURrrrrrrrrrrrrr!')

  def turn (self, direction):
    print(f'The {self.make} {self.model} turned {direction} on a dime like no other car can ')


my_car = SUV()
my_car.make = "Saturn"
my_car.model = "Vue"
my_car.year = "2005"
my_car.main_color = "Blue"

curts_car = Coup()
curts_car.make = "Nissan"
curts_car.model = "Sentra"
curts_car.year = "2009"
curts_car.main_color = "gold"

scotts_car = Sedan()
scotts_car.make = "Hyundai"
scotts_car.model = "Senata"
scotts_car.year = "2015"
scotts_car.main_color = "Blue"

joes_car = Sports_car ()
joes_car.make = "Chevy"
joes_car.model = "Corvette"
joes_car.year = "1965"
joes_car.main_color = "Red"

drews_car = Truck()
drews_car.make = "Ford"
drews_car.model = "F150"
drews_car.year = "1989"
drews_car.main_color = "Black"



my_car.drive()
my_car.turn("right")
my_car.stop()
joes_car.drive()
joes_car.turn("right")
joes_car.stop()
curts_car.drive()
curts_car.turn("right")
curts_car.stop()
drews_car.drive()
drews_car.turn("right")
drews_car.stop()
scotts_car.drive()
scotts_car.turn("right")
scotts_car.stop()