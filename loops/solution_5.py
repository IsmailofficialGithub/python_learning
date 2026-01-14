print('Find the first Non-Repeated Character from String')

string ='Banadna'

for char in string:
    if string.count(char)==1 :
        print('Non repeated Char is :',char)
        exit()
        