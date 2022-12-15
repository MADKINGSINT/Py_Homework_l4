
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# from random import randint
# k = int(input('Введите коэффициент: '))
# sp=[]
# for el in range(1, k+2):
#     sp.append(randint(1, 9))
# print(sp)

# STr_to_file = ''

# for i in range (0, len(sp)):
#     if i == len(sp) - 1 :
#         print(sp[i])
#         STr_to_file += (str(sp[i]))
#         break 

#     print (f"{sp[i]}*X^{k}+", sep='', end='' )
#     STr_to_file += (f"{sp[i]}*X^{k} + ")        
#     i +=1
#     k -=1
# print (STr_to_file)

# data = open ('HomeWorkL4/file.txt', 'w')
# data.write(STr_to_file)
# data.close
#ДЛЯ ДВУХ ФАЙЛОВ К 5 ЗАДАЧЕ
from random import randint
k = int(input('Введите коэффициент: '))
r2=k
sp=[]
sp2=[]
for el in range(1, k+2):
    sp.append(randint(1, 9))
print(sp)

for el in range(1, k+2):
    sp2.append(randint(1, 9))
print(sp2)

STr_to_file = ''

for i in range (0, len(sp)):
    if i == len(sp) - 1 :
        print(sp[i])
        STr_to_file += (str(sp[i]))
        break 

    print (f"{sp[i]}*X^{k}+", sep='', end='' )
    STr_to_file += (f"{sp[i]}*X^{k} + ")        
    i +=1
    k -=1
print (STr_to_file)

data = open ('HomeWorkL4/file1.txt', 'w')
data.write(STr_to_file)
data.close

STr_to_file2 = ''

for i in range (0, len(sp2)):
    if i == len(sp2) - 1 :
        print(sp2[i])
        STr_to_file2 += (str(sp2[i]))
        break 

    print (f"{sp2[i]}*X^{r2}+", sep='', end='' )
    STr_to_file2 += (f"{sp2[i]}*X^{r2} + ")        
    i +=1
    r2 -=1
print (STr_to_file2)

data = open ('HomeWorkL4/file2.txt', 'w')
data.write(STr_to_file2)
data.close
    