"""demo for the IO"""

try:
    name = input('enter the name :')
    city = input('enter the city :')
    zip_code = hex(int(input('enter the postal code :')))
    print('name :', name)
    print('city :', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as error:
    print(error)
except Exception as error:  # generic handler
    print('generic :', error)
