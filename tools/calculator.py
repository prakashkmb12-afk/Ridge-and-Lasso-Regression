def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "Invalid calculation"