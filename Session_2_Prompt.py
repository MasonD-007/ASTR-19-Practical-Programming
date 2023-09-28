"""
Write a Python that prints the sum of two floating point numbers, 
the difference between two integers, 
and the product of a floating point number and an integer. 
In each case, have the program print out the data type of the resulting answer.
"""
def difference(x, y): 
    difference = x - y
    return difference

def product(x, y):
    product = x * y
    return product

def sum(x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    sumAns = sum(float(1.5), float(2.5))
    diffAns = difference(int(5), int(2))
    prodAns = product(float(2.5), int(5))
    print("The sum of two floating point numbers is: ", sumAns)
    print("The difference between two integers is: ", diffAns)
    print("The product of a floating point number and an integer is: ", prodAns)