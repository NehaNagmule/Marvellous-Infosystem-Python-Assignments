# Definition of Addition
def Add(no1, no2):
    ans = no1 + no2
    return ans


# Definition of Subtraction
def Sub(no1, no2):
    ans = no1 - no2
    return ans


# Definition of Multiplication
def Mult(no1, no2):
    ans = no1 * no2
    return ans


# Definition of Division
def Div(no1, no2):

    if no2 != 0:
        ans = no1 / no2
        return ans
    else:
        return "undefined"
