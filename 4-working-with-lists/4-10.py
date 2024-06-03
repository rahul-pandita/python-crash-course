# SLICES
# : Using one of the programs you wrote in this chapter, add several 
#lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are: Then use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Then use a slice to print the last three items in the list

multiples_of_three = list(range(3, 31, 3))

for num in multiples_of_three:
    print(num)

print(multiples_of_three)
print(f"The first three items in the list are: {multiples_of_three[:3]}.")
print(f"Three items from the middle of the list: {multiples_of_three[:]}")