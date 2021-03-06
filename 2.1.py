#Циклы
#1
#Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
# и после первого введенного нуля выводит сумму полученных на вход чисел.
a=1
s=0
while True:
    a=int(input())
    if a!=0:
        s+=a
    if a==0:
        break
print(s)
#or
a = int(input())
s = 0
while a != 0 :
    s += a
    a = int(input())
print(s)
#or
s, n =0, int(input())
while n:
    s, n = s + n, int(input())
print(s)
#or
#3
#Программа должна считывать размеры команд (два положительных целых числа aa и bb,
#каждое число вводится на отдельной строке) и выводить наименьшее число dd, которое делится на оба этих числа без остатка.
a=int(input())
b=int(input())
d=a
while d>0:
    if d%b==0:
        break
    d+=a
print(d)
#or
a = int(input())
b = int(input())
d = a
while d%b:
    d += a
print(d)
#or
from fractions import gcd
a, b = int(input()), int(input())
print(int((a*b)/gcd(a,b)))
#4
#Для каждого введённого числа проверить:
#если число меньше 10, то пропускаем это число;
#если число больше 100, то прекращаем считывать числа;
#в остальных случаях вывести это число обратно на консоль в отдельной строке.
x=1
while x>0:
    x=int(input())
    if x<10:
        continue
    elif x>100:
        break
    else:
        print(x)
#or
a = 0
while a <= 100:
    a = int(input())
    if 10 <= a <= 100:
        print(a)
#5
#Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
#Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b][a;b] на все числа отрезка [c;d][c;d].
#Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a≤ba≤b, c≤dc≤d.
a=int(input())
b=int(input())
c=int(input())
d=int(input())
a<=b and c<=d and b<10 and d<10
for i in range(c, d + 1):
    print('\t', i, end='')
print()
for j in range(a, b+1):
    print(j, end='\t')
    for k in range (c, d + 1):
        print(j*k, end='\t')
    print()
#6
#Напишите программу, которая считывает с клавиатуры два числа a и b,
#считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b][a;b], которые делятся на 33.
a=int(input())
b=int(input())
s=0
n=0
for i in range(a, b+1):
    if i%3==0:
        s+=i
        n+=1
    if i==b:
        print(s/n)
#or
x = [x for x in range(int(input()),int(input()) + 1) if x % 3 == 0]
print(sum(x)/len(x))
#or
import statistics
a = int(input())
b = int(input())
l = [i for i in range(a, b + 1) if i % 3 == 0]
print(statistics.mean(l))
#7
#GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение
#суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
#Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин)
#в введенной строке (программа не должна зависеть от регистра вводимых символов).
x=input().upper()
c=x.count('G')
b=x.count('C')
print(((c+b)/len(x))*100)
#or
s = input().upper()
print((s.count('G') + s.count('C'))/len(s) * 100)
#or
a=input().upper()
print(((a.count('C')+a.count('G'))/len(a))*100)
#8
#Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты
#группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
#Кодирование осуществляется следующим образом:
#s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на
#этот символ и количество его повторений в этой позиции строки.
#Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит
#закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
genome = input()+' '
s = 0
n=genome[0]
for i in genome:
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1
#or
import re; print(re.sub(r'(.)(\1)+|(.)', lambda m: m.group(0)[0] + str(len(m.group(0))), input()))
#or
g = str(input())
rep = 1
out = g[0]
for i in range(1,len(g)):
  if (g[i] == g[i-1]):
    rep +=1
  else:
    out = out+str(rep)+g[i]
    rep=1
print(out+str(rep))
#or
import itertools
print("".join([k+str(len(list(g))) for k, g in itertools.groupby(input())]))
#9
#Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
a=[int(i) for i in input().split()]
print(sum(a))
#or
a=[int(i) for i in input().split()]
s=0
for i in a:
    s+=i
print(s)
#or
s = 0
for i in input().split():
    s += int(i)
print(s)
#10
#Напишите программу, на вход которой подаётся список чисел одной строкой.
#Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
#Для элементов списка, являющихся крайними, одним из соседей считается элемент,
#находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10",
#то на выход ожидается список "13 6 9 15 7" (без кавычек).
#Если на вход пришло только одно число, надо вывести его же.
#Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
numbers = [int(i) for i in input().split()]
if len(numbers) == 1:
    print(numbers[0])
else:
    for i in range(len(numbers)):
        print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")
#or
x = [int(i) for i in input().split(' ')] #создаем список, напр [1, 2, 3, 4, 5]

if len(x) <=1:
    print (x[0])
else:

    y = [x[i-1] for i in range(len(x))] #массив перестановка вправо [5, 1, 2, 3, 4]
    z = [x[i] for i in range(-len(x)+1,1)] #массив перестановка влево [2, 3, 4, 5, 1]

    for i in range(len(x)): print(y[i]+z[i], end=' ') #теперь просто поэлементно сложить
#11
#Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран
# в одну строку значения, которые повторяются в нём более одного раза.
#Для решения задачи может пригодиться метод sort списка.
#Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')
#or
a = [int(i) for i in input().split(" ")]
b=[]
for i in a:
    if (a.count(i)>1) and (not i in b):
        b.append(i)
for i in b:
    print(i, end=' ')
#or
s  = [int(i) for i in input().split()]
temp = []
for char in s :
    if s.count(char) > 1 and char not in temp :
        temp += [char]
        print(char,end = ' ')
#12
#Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
#пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
#Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
#В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна
#нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.
a=1
s=0
sq=0
while True:
    a=int(input())
    s+=a
    sq+=(a*a)
    if s==0:
        break
print(sq)
#or
s=[int(input())]
while sum(s)!=0: s.append(int(input()))
print(sum([i**2 for i in s]))
#13
#Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
#(число повторяется столько раз, чему равно). На вход программе передаётся положительное целое число n
# — столько элементов последовательности должна отобразить программа.
#На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])
#or
n, a = int(input()), []
for i in range(1, n + 1): a += ([i] * i)
print(*a[:n])
#or
print(*(lambda n: ("".join((str(x) + " ") * x for x in range(1, n + 1))).split()[:n])(int(input())))
#14
#Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
#которая выводит все позиции, на которых встречается число xx в переданном списке lst.
#Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
#Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
l = [int(i) for i in input().split()]
x = int(input())
if not x in l: print('Отсутствует')
for i in range(len(l)):
    if l[i]==x: print(i, end = ' ')
#or



























