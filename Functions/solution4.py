print('create a function that take multiple parameters and returns there sum')

def mul_function(*value):
    sum=0
    for i in value:
        sum+=i
    return sum

result=mul_function(1,2,3,5,4)

print("Sum of Given numbers : ", result)


