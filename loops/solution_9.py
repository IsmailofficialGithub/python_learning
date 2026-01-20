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
