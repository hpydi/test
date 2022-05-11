#Calculator function factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("please Enter integer number: "))
result1 = factorial(number)
#Calculator function square
def sqrt(a):
    return a**0.5
result2= round(sqrt(result1))
#Calculator even number and added to list
def even(number):
    list = []
    index = 0
    while index < number:
        if index % 2 == 0:       
            list.append(index)
        index = index + 1
    return list
myList=(even(result2))
print(myList)
#Convert list to dict
def listToDict(list1):
    op = { i : list1[i] for i in range(0, len(list1) ) }
    return op
list1=(myList)
print(listToDict(list1))