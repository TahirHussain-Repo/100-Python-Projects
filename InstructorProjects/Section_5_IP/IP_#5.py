import pandas as pd

employee_data = pd.read_excel('employee_data.xlsx')
print(employee_data.head())
print(employee_data.info())
print(employee_data.describe())


employee_data['Bonus'] = employee_data['Salary'] * 0.1

print(employee_data)

employee_data.to_excel('employee_data_with_bonus.xlsx', index=False)