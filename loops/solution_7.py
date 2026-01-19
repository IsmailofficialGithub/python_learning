print('Validate the number if its between 1 to 10 else again get input from user')
while True:
    number=int(input('Enter Value Between 1 and 10 : '))

    if 1 <=number <= 10:
        print('Thanks ')
        break
    else:
        print('Invalid Number , Try again')
    
    