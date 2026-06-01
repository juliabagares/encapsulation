class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, status):
        self.__on = status

    def display(self):
        status = "ON" if self.__on else "OFF"
        print(f"""
fan status: {status}
speed: {self.__speed}
radius: {self.__radius}
color: {self.__color}
""")

fan_1 = Fan(Fan.FAST, 10, "yellow", True)
fan_2 = Fan(Fan.MEDIUM, 5, "blue", False)

print(fan_1.display())
print(fan_2.display())