<<<<<<< HEAD
print('Check if all elements in a list are unique . If a duplicate is found , exit the loop and print the duplicate')

items=['apple','banana','orange','apple','mango']

for i in items :
    for j in items :
        if(i == items[j]):
            print(items[j],' is a dublicate number')
            break
=======
print('Check any dublicate item in list')

items=['apple','banana','orange','grapes']

unique_item=set()

for item in items:
    if item in unique_item:
        print('Dublicate :',item)
        break
    unique_item.add(item)
else:
    print("No Dublicate item in list")
>>>>>>> a775ceb607429282fcde6df328a63cff22cb3254
