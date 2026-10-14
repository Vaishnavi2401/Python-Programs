## addition of 2 list elements using map function

number_1 = [1,4,5,8]
number_2 = [8,5,6,7]

print("Addition of 2 list elements are", list(map(lambda x,y: x+y, number_1, number_2)))