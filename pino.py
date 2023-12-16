import math
size = 40
left = 50
j = 1
#For para el árbol
for i in range(0,size,2):
    #espacios a la izquierda
    row = (left + math.ceil(size / 2) -j) * " "
    #asteriscos
    row += i * "@"
    j += 1
    print("\033[1;32m"+row)
#Tronco del árbol
row = (left + math.ceil (size / 2) - 3) * " "
row += 4 * "*"
print("\033[1;31m"+row)
print("\033[1;31m"+row)