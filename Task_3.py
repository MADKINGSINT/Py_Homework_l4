# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
from random import randint
list_size = int(input('enter list size:   '))
sp = []
def Fill_list(list_size, sp):
    for i in range (0 , list_size):
       sp.append(randint(0, 9))
    print(*sp)
Fill_list(list_size, sp)
   
nl = []
[nl.append(i) for i in sp if i not in nl]
print(nl)           
        



