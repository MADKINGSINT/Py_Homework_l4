#     Вычислить число c заданной точностью d
#     Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#         print(i)
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")
# print(lst)



from math import pi
count = 0
d = (input("Введите число :\n"))
for i in range(0 , len(d)):
    if d[i].isdigit() == False:
        i +=1
        for j in range (i, len(d)):
            count +=1

print(f'число Пи с заданной точностью {d} равно {round(pi, count)}')