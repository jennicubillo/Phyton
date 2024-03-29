# -*- coding: utf-8 -*-
"""03_Strngs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c6ToKdifiAwk_BwP4j9xsbh_JfHNGjiJ
"""

### Strings ###

my_string = "Mi string"
my_other_string = 'My otro string'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un sting\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age, = "Jenni", "Cubillo", 15
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es" + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

languaje = "python"
a, b, c, d, e, f, = languaje
print(a)
print(e)

# División

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:]
print(languaje_slice)

languaje_slice = languaje[-2]
print(languaje_slice)

languaje_slice = languaje[0:6:2]
print(languaje_slice)

# Fuciones del lenguaje
#print(language.capitalice())
#print(language.upper())
#print(language.count("t"))
#print(language.isnumeric())
#print("1".isnumeric())
#print(language.lower())
#print(language.lower().isupper())
#print(language.startswitch("Py")
#print("Py" == "py") # No es lo mismo