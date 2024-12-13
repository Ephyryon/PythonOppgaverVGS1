

#Checks if input is in a list inside of a list
def check_input(input_value, list_of_lists):
    for sublist in list_of_lists:
        if input_value in sublist:
            return True
    return False

#Checks if "s" is a float number
def is_num_f(s):
        try: 
            float(s)
            return True
        except ValueError:
            return False

#Checks if "s" is a int number
def is_num_i(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Checks if dividend can be divided by the divisor
def can_div(dividend, divisor):
    if dividend % divisor == 0:
        return True