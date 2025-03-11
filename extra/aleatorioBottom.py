import os
os.system("clear")


class Person:
  def __init__(self, name, age):
    self.name = input("DIgite seu nome: ")
    self.age = input("DIgite sua idade: ")

  def myfunc(self):
    print(f"Meu nome é {self.name} e tenho {self.age} anos de idade.")

p1 = Person("John", 36)
p1.myfunc()