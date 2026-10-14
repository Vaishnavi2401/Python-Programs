employee = [{'Name':'Vaishnavi', 'Age': 25, 'Salary': 25000},
            {'Name':'Shital', 'Age': 26, 'Salary': 30000},
            {'Name':'Amit', 'Age': 27, 'Salary': 35000},
            {'Name':'Juhi', 'Age': 28, 'Salary': 40000}]

print(list(filter(lambda x: x['Age'] > 26, employee)))