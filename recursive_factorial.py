def factorial_recursive(num):
    if(num ==1 or num == 0):
        return 1
    else:
        return num * factorial_recursive(num-1)

number = int(input("enter a number to find factorial:"))

result = factorial_recursive(number)
print(f"factorial of {number} is : {result}") 