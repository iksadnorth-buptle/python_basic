# section07-2

# 예제1
# 상속 기본
class Car:
    """Parent Class"""
    def __init__(self, tp, color) -> None:
        self.tp = tp
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'
    
class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color) -> None:
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        super().show()
        return "Your Car Name : %s" % self.car_name
    
class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color) -> None:
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        return 'Car Info : %s %s %s' % (self.car_name, self.tp, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.tp) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", "suv", "black")
print(model2.show())
'''
red
sedan
520d
Car Class "Show Method!"
Your Car Name : 520d
Car Info : 220d suv black
'''

# Parent Method Call - super를 이용해 부모 메서드에 접근
model3 = BmwCar("220d", "suv", "black")
print(model3.show_model())


print()

# Inheritance Info
print(BmwCar.mro())

