price = int(input("How much is the item? "))

if price <= 10:
    print("Your item is cheap")
elif price <= 50:
    print("Your item is affordable")
elif price <= 100:
    print("Your item is  moderate")
else: 
    print("Your item is expensive")