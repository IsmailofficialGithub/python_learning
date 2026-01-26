print('Check if all elements in a list are unique . If a duplicate is found , exit the loop and print the duplicate')

items=['apple','banana','orange','apple','mango']

for i in items :
    for j in items :
        if(i == items[j]):
            print(items[j],' is a dublicate number')
            break