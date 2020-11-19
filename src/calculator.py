TYPE_ERROR = 'is not a number'
SIGN_ERROR = 'Operation sign is wrong'


def validate(number1, operation, number2):
  type_number1 = type(number1)
  type_number2 = type(number2)

  if type_number1 != int and type_number1 != float:
    print(f"{number1} {TYPE_ERROR}")
    return False

  if type_number2 != int and type_number2 != float:
    print(f"{number2} {TYPE_ERROR}")
    return False

  if operation != '+' and operation != '-' and operation != '*' and operation != '/':
    print(SIGN_ERROR)
    return False

  return True


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

