#Define variables to store the following item categories and their quantities as integers 
fruits= 200
vegetables= 150
dairy = 100
baked_goods= 75
#Calculate the total number of items in the inventory
inventory = fruits + vegetables + dairy +baked_goods
#Add 20 more dairy items to the inventory
#note for future, instead of changing the variable, keep the same. The updated version of the variable will be printed
updated_dairy= dairy + 20
#Check if the number of Baked Goods are greater than or equal to 70 and store the result in a variable 
a = baked_goods>= 70
#Print out the inventory item by item with their quantities 
print("Fruits", fruits, "Vegetables", vegetables, "Dairy", updated_dairy, "Baked Goods", baked_goods)
#Print out the total number of items
print(fruits + vegetables + updated_dairy + baked_goods)
#Print True or False indicating whether the number of baked goods is greater than or equal to 70
print(a)