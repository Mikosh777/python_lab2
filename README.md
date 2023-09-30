#Task 1
number=int(input("Enter four-digit number: "))
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10
if thousands+units==hundreds-tens:
    print('YES')
else:
    print('NO')
    
#2 Roskomnadzor

age=int(input('Enter an age: '))
if age>=18 :
    print('Access is allowed ')
else:
    print('Access denied  ')
    
#3 Arithmetic progression 

num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
num3=int(input('Enter num3: '))

q1=num2-num1
q2=num3-num2

if q2==q1:
    print('YES')
else:
    print('no')
    
    # 4 Rook move

a = int(input('x position: '))
b = int(input('y position: '))
c = int(input('next x position: '))
d = int(input('next y position: '))

if(a!=c and b==d or a==c and b!=d):
    print("Yes")
else:
    print("No")
    
    
#  5 KingsMove

a = int(input('x position: '))
b = int(input('y position: '))
c = int(input('next x position: '))
d = int(input('next y position: '))

if ():
     print("Yes")
else:
     print("No")
     
     
#6

x=int(input())
y=int(input())
z=int(input())

avr_num=x+y+z
avr_num/=3
print(avr_num)
