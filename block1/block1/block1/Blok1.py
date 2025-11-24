import math
#Лекція 3
#1
a = float(input())
print (int(a))
#2
a = int(input())
print(str(a),"!")
#3
a= int(input())
b= int(input())
print(f"Ці числа утворюють множину:{a},{b}")
#4
a = str(input("Як вас звати?"))
print ("Привіт",str(a))
#sep=";"
#Лекція 4
#1
a = int(input())
print((((a+2)**3)/4)-5)
#2
a = float(input("Введіть a:"))
b = float(input("Введіть b:"))
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)
print(b,'/',a,'=',b/a)
#3
a = float(input("Введіть a:"))
b = float(input("Введіть b:"))
c = float(input("Введіть c:"))
print(max(a,b,c))
print(min(a,b,c))
#4
a= int(input("Введіть число"))
x = a/7
print ("x = ",float(x))
x = 15/a
print ("x = ",float(x))
#5
a = 3,17
b = 20,56
c = b-a
print(int(c))

a = 2
b = 56,2
c = b-a
print(int(c))

a = 34 + 45,13
b = 147
c = b-a
print(int(c))

#6
a = int(input())
b = bin(a)
c = hex(a)
print(b,c,sep=";")
#7
a = int(input())
b = str(input())
print(a*b)

#Лекція 5
#1
a = int(input())
b = int(input())
print(a**b,b**a,a**b-1,b**a-1,(a*b)**a+b)
#2
a=int(input())
print(4*a*math.pi)

#3
a = int(input())
print(math.factorial(a))

#Лекція 6
#1
#а
a= int(input())
print(a>0)
#б
a= int(input())
b = int(input)
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a**2>b**2)
print(a+b>a*b)

#2
a= int(input())
b= int(input())
a1 = int(a/10)
a2 = int(a%10)
b1 = int(b/10)
b2 = int(b%10)
print((a1+a2)==(b1+b2))
#Лекція 7
# 1
a = int(input()) 
if(a>0 and a<100):
    print("Число входить в проміжок")
else:
    print("Число не входить в проміжок")
#2
a = int(input())
if(a>=-33 and a==151):
    print("Число входить в проміжок")
else:
    print("Число не входить в проміжок")

#3

a = float(input())
if(a > -100 and a < 100 ):
    print("Число входить в проміжок")
else:
    print("Число не входить в проміжок")

4
a= int(input())
b= int(input())
c= int(input())

l = 0.0
m = 0.0
h = 0.0

if a < b and a < c:
    l = a
elif b < a and b < c:
    l = b
else:
    l = c

if a > b and a > c:
    h = a
elif b > a and b > c:
    h = b
else:
    h = c

m = (a + b + c) - l - h

print(a,b,c,sep = "<")

5
a = float(input())
b = float(input())
c = float(input())

if (a+b==c):
    print("Трикутник існує")
elif (a+c==b):
    print("Трикутник існує")    
elif (c+b==a):
    print("Трикутник існує")
else:
    print("Трикутник не існує")

#6
a= float(input())
b= float(input())

x = (a/b)+3

print(x)

#7
a = float(input())
b = float(input())
c = float(input())

x1 = (c + math.sqrt(25*c**2 + 4*c*(a + b))) / (2*c)
x2 = (c - math.sqrt(25*c**2 + 4*c*(a + b))) / (2*c)

print(x1)
print(x2)

# Лекція 8
#1
a=int(input())
while a< 100:
    a=a+5
    print(a)

2
a = int(input("Введіть а:"))
b = int(input("Введіть b:"))
while a!=b:
    b=int(input("Спробуйте ще раз вгадати число a"))

print("Ви вгадали число а =", a)

3
a = 1000
print("Початковий внесок:", a)
n = int(input("Введіть кількість років:"))
c=0
while c<n:
    a*0.25
    c+=1
4
a=int(input("Введіть а:"))
n=int(input("Введіть n:"))
c=0
while n>a:
    a+=5
    c+=a
print("Сума чисел дорівнює:", c)
5
a=int(input("Введіть факторіал:"))
while a>a+1:
    a*=a-1
print("Факторіал дорівнює:", a)

