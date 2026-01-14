print('Reverce a String using a loop')

# solution

string = 'Hi, I am string'
reverse_string=''

for i in string:
    reverse_string=i + reverse_string 
print(reverse_string)