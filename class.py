class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print('Started')
    
    def stop(self):
        print('Stopped')
    
    def accelerate(self):
        print('accelerating...')
        #Accelerating functionality here

    def changeGear(self):
        print('Gear Changed')
        #Gear related functionality here

audi = Car("A7", "grey", "audi", "450 km/ph")
print(audi.color)
print(audi.model)
print(audi.changeGear())
print(audi.accelerate())

