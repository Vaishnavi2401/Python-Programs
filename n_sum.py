# printing the sum of first n natural numbers
n_value = int(input("Enter the value for n:"))

sum =0
for i in range(1, n_value+1):
    sum +=i
print(f"The sum of first {n_value} natural numbers is : {sum}")