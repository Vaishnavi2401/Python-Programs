print("list demo: ")

lists = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
text_list = ["Apple", "Banana", "Carrot", "Dragon fruit"]

print("1st list: ", lists)
print("2nd list: ", text_list)

# append function

lists.append(7)
print("after append 1st list: ", lists)

lists.insert(1, 8)
print("after inserting 8 at 1st index - 1st list: ", lists)

lists.remove(6)
print("after removing 6 - 1st list: ", lists)

lists.pop(2)
print("after poping 2nd index value - 1st list: ", lists)

index_5 = lists.index(5)
print("value at index 5: ", index_5)

count_list = lists.count(8)
print("to count no of 8 present in list: ", count_list)

lists.sort()
print("sorted list: ", lists)

lists.reverse()
print("reverse list: ", lists)

lists.clear()
print("clear list: ", lists)

# enumerate
print("enumerate output of 2nd list: ")
for index_value, value in enumerate(text_list):
    print(index_value, value)

#length
print("length of 2nd list:", len(text_list))

#list comprehension:

list_items = [x for x in range(1, 51)]
print("list comprehension example list from 1 to 50: ",list_items)

even_items = [x**2 for x in range(1, 51) if x%2 == 0]
print(" list of sqr of even from 1 to 50: ",even_items)

#function in list comprehension:
length_list = [len(word) for word in text_list]
print("length_list of text_list", length_list)

#list pair example
pair = [[i,j] for i in text_list for j in length_list]
print("pair of 2 lists:", pair)
