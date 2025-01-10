import pandas as pd

input_data = pd.read_excel('Input.xlsx')

print(input_data)


input_data['Total'] = input_data['Price'] * input_data['Quantity']

print(input_data)

input_data.to_excel('output.xlsx', index=False)