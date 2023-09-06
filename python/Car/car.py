class Car :
    steeringWheel=1                 #class level attribute

    @classmethod                    #class level method
    def common(cls):
        print(f'all car have only {cls.steeringWheel} steeringWheel')

    def __init__(self,name,wheel): 
        self.name=name              #instant level attribute
        self.wheels=wheel           #instant level attribute

    def drive(self):                #instant method
        print(f'{self.name} is driving')
    
toyota=Car("Toyota",4)
print(toyota.wheels)
toyota.drive()

marcedes=Car("Marcedes",4)
marcedes.drive()

print(Car.steeringWheel)

lambo=Car("lambo",4)
lambo.common()