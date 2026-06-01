class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def display(self):
        print(f"{self.__year_model} {self.__make} | Speed: {self.__speed} km/h")

car=Car("2023", "Mustang")

print("Accelerating Car")
for i in range(5):
    car.accelerate()
    car.display()


