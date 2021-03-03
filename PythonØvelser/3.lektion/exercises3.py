import sys
#

# Ex.2
# 1. From 2 lists, using a list comprehension, create a list containing:


colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

clothesList = [(i, j) for i in colors for j in sizes]
print(clothesList)

# 2. If the tuple pair is in the following list, it should not be added to the comprehension generated list.

sold_out = [('Black', 'm'), ('White', 's')]

clothesList2 = [item for item in clothesList if item not in sold_out]
print(clothesList2)


print("this is the name of the script", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))
