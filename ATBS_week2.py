'''---------------------
----ATBS_week1.py-------
-----by PJ Sheldon------
---------------------'''
#inventory function
def displayInventory(inventory):
	print("Inventory: ")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + " " + k)
		item_total = item_total + v
	print("Total number of items: " + str(item_total))
#add to inventory function
def addToInventory(inventory, addedItems):
	for k in range(len(addedItems)):
		inventory.setdefault(addedItems[k], 0)
		inventory[addedItems[k]] += 1
	return(inventory)			

stuff = {'rope' : 1, 'touch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12} # inforamtion from the previous set
inv = {'gold coin' : 42, 'rope' : 1} # current loot
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin','ruby'] # new loot
displayInventory(inv) 
print("Your Inventory is now updated! Thanks for playing!") # updated message