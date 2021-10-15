with open('ex_3.txt', 'r', encoding='utf-8') as f_3:
    surnames = []
    average_income = 0
    string = 0
    for line in f_3:
        string += 1
        surname, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            surnames.append(surname)
        average_income += income
    average_income = average_income / string
print(f'Surnames of employees with income over 20,000:')
print(*surnames)
print(f'\nAverage income of all employees:\n{average_income}')
