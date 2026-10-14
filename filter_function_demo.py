# filter even numbers from a list using filter function

def even_function(value):
    if value % 2 ==0:
        return True
    else: 
        return False

iterable_list = [2,3,9,12,5,45,99,9,7,88,8,6,4,2,1]

print(list(filter(even_function, iterable_list)))

    