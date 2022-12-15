
# MC1 = str([])
data1 = open ('HomeWorkL4/file1.txt', 'r')
st = (data1.read())
data1.close
# MC2 = str2([])
data2 = open ('HomeWorkL4/file2.txt', 'r')
sr2 = (data2.read())
data2.close
print(("первый многочлен"),st)
print(("второй многочлен"),sr2)

s = st
l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))



d=[]
for i in range(0,len(integ),2):
    d.append(integ[i])

s2 = sr2
l = len(s2)
integ2 = []
i = 0
while i < l:
    s2_int = ''
    a = s2[i]
    while '0' <= a <= '9':
        s2_int += a
        i += 1
        if i < l:
            a = s2[i]
        else:
            break
    i += 1
    if s2_int != '':
        integ2.append(int(s2_int))



d2=[]
for i in range(0,len(integ2),2):
    d2.append(integ2[i])

c=[]

c = [x+y for x, y in zip(d, d2)] 

from random import randint

k=(len(c)-1)
STr_to_file = ''

for i in range (0, len(c)):
    if i == len(c) - 1 :
        STr_to_file += (str(c[i]))
        break 

    STr_to_file += (f"{c[i]}*X^{k} + ")        
    i +=1
    k -=1
print (("сумма многочленов"),STr_to_file)

data = open ('HomeWorkL4/file_sum.txt', 'w')
data.write(STr_to_file)
data.close









#🎅