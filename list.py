# name = "shani"
# print(name[1])
# name[1] = "s"
# print(name)                             # example of  string are immutable
# second_name = name[3]
# print(second_name)


        # LIST(array): are containers used to store multiple values of different data type in python 
l1 = [1,2,5,5,4,6,2,6,4,3,4]
list = ["shani","hammad","moin",2,4,True,None,3454.34,"yellow"]
list[4] = "tester"
print(list[0:5])
list.append("sufyan")  # append is used to Adds an item x to the end of the list.
l1.sort()   # to sort itens in sequence
l1.reverse() # Reverses the order of items in the list, modifying it in place.
list.insert(3,"hunter")  # Inserts an item "hunter" at index 3.
list.pop(0)   #Removes and returns the item at index i. If i is not specified,
            #    removes and returns the last item.
l1.remove(1)   # Removes the first occurrence of x in the list.

print(list)
print(l1)

print(list.index("yellow"))   #Returns the index of the first occurrence of "yellow".
print(l1.count(5))    # Returns the number of occurrences of 5 in the array.