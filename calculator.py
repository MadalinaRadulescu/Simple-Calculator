def is_number(str):
    if str.isnumeric() is True:
        return True
    elif str.lstrip("-").isnumeric() is True:
        return True
    try:
        float(str)
        return True
    except ValueError:
        return False

def convert_number(str):
    if is_number(str) is True:
        try:
            str = int(str)
            return str
        except ValueError:
            return str
    

def is_valid_operator(operator):
    if operator == "+":
        return True
    elif operator == "-":
        return True
    elif operator == "*":
        return True
    elif operator == "/":
        return True
    else:
        return False


def ask_for_a_number(force_valid_input):
    while True:
        num = input("Please provide a number! ")
        if is_number(num) is True:
            return convert_number(num)
        else:
            if not force_valid_input:
                return None
            print("This didn't look like a number, try again.")
            
            
            

def ask_for_an_operator(force_valid_input):
    while True:
        oper = input("Please provide an operator (one of +, -, *, /)!")
        if is_valid_operator(oper) is True:
            return oper
        else:
            if not force_valid_input:
                return None
            print("Unknown operator.")


def calc(operator, a, b):
    if not is_valid_operator(operator):
        return None
    result = None
    if operator == "+":
        result = a + b
        return result
    elif operator == "-":
        result = a - b
        return result
    elif operator == "*":
        result = a * b
        return result
    elif operator == "/":
        if b == 0:
            print("Error: Division by zero")
            return None
        else:
            result = a / b
            return result


def simple_calculator():
    while True:
        a = ask_for_a_number(force_valid_input=False)
        if a is None:
            break
        op = ask_for_an_operator(force_valid_input=True)
        b = ask_for_a_number(force_valid_input=True)
        result = calc(op, a, b)
        if result is not None:
            print(f"The result is {result}")

if __name__ == '__main__':
    simple_calculator()
