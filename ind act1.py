 #Define variables to store the following book genres and their quantities as integers
fiction = 120
non_fiction= 80
science = 60
history = 40
#Calculate the total number of books in inventory
inventory=fiction + non_fiction + science + history
print(inventory)
#Add 10 books to the fiction inventory
a = fiction + 10
print(a)
#Check if the number of Science books is less than or equal to 50 and store the result in a variable
b=science <= 50

#Print out the inventory item by item with their quantities
print("Fiction", a, "Non-Fiction", non_fiction,"Science", science, "History", history ) 
#Print the total number of books 
print(inventory+10)
#Print True or False indicating whether the number of Science books is less than or equal to 50
print(b)