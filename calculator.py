"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def get_user_equation():
    # asks for input 
    # user_equation variable stores their input
    print("Please use the following format: operator num1 num2 (i.e. + 2 3)")
    user_equation = input("Enter Equation: ")
    return user_equation

def get_calculation():
# repeat forever:
    while True:

#     read input call get_user_equation function to receive user input
        input_string = get_user_equation()
#     tokenize input
        tokens = input_string.split(" ")
#         if the first token is "q":
        if tokens[0] == "q":
#             quit
            print("Exit Calculator")
            quit()
#         else:
        else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens
            if tokens[0] == "pow":
                print(power(int(tokens[1]), int(tokens[2])))

#             elif the first token is "+":
#                   call the add function with the other two tokens 
            elif tokens[0] == "+":
                print(add(int(tokens[1]), int(tokens[2])))

#             elif the first token is "-":
#                   call the subtract function with the other two tokens 
            elif tokens[0] == "-":
                print(subtract(int(tokens[1]), int(tokens[2])))

#             elif the first token is "*":
#                   call the multiply function with the other two tokens 
            elif tokens[0] == "*":
                print(multiply(int(tokens[1]), int(tokens[2])))

    #             elif the first token is "/":
    #                   call the divide function with the other two tokens 
            elif tokens[0] == "/":
                print(divide(int(tokens[1]), int(tokens[2])))

    #             elif the first token is "square":
    #                   call the square function with the other two tokens 
            elif tokens[0] == "square":
                print(square(int(tokens[1])))

    #             elif the first token is "cube":
    #                   call the cube function with the other two tokens 
            elif tokens[0] == "cube":
                print(cube(int(tokens[1])))

    #             elif the first token is "mod":
    #                   call the mod function with the other two tokens 
            elif tokens[0] == "mod":
                print(mod(int(tokens[1]), int(tokens[2])))

get_calculation()