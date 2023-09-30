#1 Ratio
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
    
    
#  5 Kings Move
a = int(input('x position: '))
b = int(input('y position: '))
c = int(input('next x position: '))
d = int(input('next y position: '))

if ():
     print("Yes")
else:
     print("No")
     
     
#6 Average number
x=int(input())
y=int(input())
z=int(input())

array = [x, y, z]
array.sort()
print(array[1])

#7 Number of days
try:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(input("input month:"))
        print(days[month])
except ValueError:
        print("Value should be Integer!")

#8 Weigh-in ceremony 
try:
    kg = int(input("Enter weight:"))
    if kg <= 60 :    print("Light weight")
    elif kg <= 64 and kg >=60:
         print("First welterweight ")
    elif kg <= 69 and kg >=64:
         print("Welterweight ")
except ValueError:
        print("Value should be Integer!")

#9 Password 
try:
        password = input("Enter password: ")
        password_check = input("confirm your password: ")

        if password_check == password:
            print("Password accepted")
        else:
            print("Password not accepted")
except ValueError:
    print("Value should be Integer")

#10 Even or odd
try:
        num = int(input("Enter your number: "))

        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

except ValueError:
    print("Value should be Integer")

#11 The smallest of two numbers 
try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        min_number = min(num1, num2) 

        print("Minimum number is:", min_number)
except ValueError:
    print("Value should be Integer")

#12 Age Group 
try:
        age = int(input("Enter your age: "))

        if age <= 13:
            print(" inclusive-childhood")
        elif 14 <= age <= 24:
            print("youth")
        elif 25 <= age <= 59:
            print("maturity")
        else:
            print("old age")
except ValueError:
    print("Value should be Integer")

#13 Triangle view 
try:
        side1 = int(input("Enter height: "))
        side2 = int(input("Enter width: "))
        side3 = int(input("Enter length: "))

        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if side1 == side2 == side3:
                print("Equilateral")
            elif side1 == side2 or side1 == side3 or side2 == side3:
                print("Isosceles")
            else:
                print("Versatile")
        else:
            print("A triangle with such sides is impossible")

except ValueError:
    print("Value should be Integer")
