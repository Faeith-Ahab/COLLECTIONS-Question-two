#  Consider 2 lists a and b, write a program that returns a list of elements that are common within the lists without any duplicate item

a = [1, 1, 2, 3, 5, 8, 13, 21, 24, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_one = a
list_one.extend(b)
print(list_one)


# Create a dictionary to return a list of elements that doesn't return any duplicate item.

list_two = [1, 1, 2, 3, 5, 8, 13, 21, 24, 55, 89, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_two = list( dict.fromkeys(list_two) )
print(list_two)





