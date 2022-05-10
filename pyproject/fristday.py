import math
num1 = int(input("please Enter integer number: "))
result = math.factorial(num1)
num2=round(math.sqrt(result))
num3=[]
for num in range(1,num2):
    if num%2==0:
        num3.append(num)
print(num3)
dict = dict() 
for index,value in enumerate(num3):
  dict[index] = value
print(dict)