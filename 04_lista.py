# -*- coding: utf-8 -*-
"""04_lista.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_3fN4qq55sFh0-D-y5eZcP7swWDD91Yz
"""

### Lists ###
# definicion

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Jenni", "Cubillo"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y busqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) #IndexError
# print(my_other_list[-5]) #IndexError

print(my_other_list.index("Jenni"))

age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3],
print(age)

# Concatenacion

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creacion, insercion, actualizacion y eliminacion

my_other_list.append("CECyTEM")
print(my_other_list)

my_other_list.insert(1, "rojo")
print(my_other_list)

my_other_list[1] = "azul"
print(my_other_list)

my_other_list.remove("azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list = [35, 24, 62, 52, 30, 17]
my_other_list = [35, 1.77, "Jenni", "Cubillo"]

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# sublistas

print(my_new_list[1:3])

# cambio de tipo

my_list = "hola python"
print(my_list)
print(type(my_list))