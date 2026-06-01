class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name.title()

    def set_animal_type(self, animal):
        self.__animal_type = animal.title()

    def set_age(self, age):
        self.__age = age

    def display(self):
        print("\nPet Profile")
        print(f"Name : {self.__name}")
        print(f"Type : {self.__animal_type}")
        print(f"Age  : {self.__age} year(s) old")


pet = Pet()

pet.set_name(input("Pet Name: "))
pet.set_animal_type(input("Animal Type: "))
pet.set_age(int(input("Pet Age: ")))

pet.display()