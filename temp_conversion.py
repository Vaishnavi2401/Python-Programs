## temprature conversion program

def temp_changes(temp_value, unit):
    if unit == 'C':
        temprature = round((temp_value* 9/5) + 32, 2)
        print(f"The temprature for {temp_value} C is {temprature} F")
    elif unit == 'F':
        temprature = round((temp_value - 32) * 5/9, 2)
        print(f"The temprature for {temp_value} F is {temprature} C")
    else:
        print("Please enter right unit value (C/F)")

input_temp = (int(input("Enter temprature value:")))
unit = input("Enter unit value (C/F):")
temp_changes(input_temp, unit)