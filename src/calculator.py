# Napisat' kalkulator

def validate(number1, operation, number2):
  type_number1 = type(number1)
  type_number2 = type(number2)
  if type_number1 == int or type_number1 == float:
    type_number1 = True
  else:
    print('Number 1 is not a number...')
    type_number1 = False

  if type_number2 == int or type_number2 == float:
    type_number2 = True
  else:
    print('Number 2 is not a number...')
    type_number2 = False

  if operation == '+' or operation == '-' or operation == '*' or operation == '/':
    operation_sign = True
  else:
    print('Operation sign is wrong...')
    operation_sign = False

  if type_number1 == True and type_number2 == True and operation_sign == True:
    is_param_valid = True
  else:
    print('Wrong input data...')
    is_param_valid = False
  return is_param_valid

def calc(number1, operation, number2):
  is_param_valid = validate(number1, operation, number2)
  if operation == "+" and is_param_valid == True:
    result = number1 + number2
  elif operation == "-" and is_param_valid == True:
    result = number1 - number2
  elif operation == "*" and is_param_valid == True:
    result = number1 * number2
  elif operation == "/" and number2 != 0 and is_param_valid == True:
    result = number1 / number2
  else:
    result = "Everything's wrong!"
  return result

result = calc(10, '/', 100)

print(result)

