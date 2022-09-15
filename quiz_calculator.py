# -*- coding: utf-8 -*-
"""
Kunhua Wu
Date: 2020/12/19

Description of this program : 
    
    This program will be imported by the main program mental_calculation_game.
    
    This program will return the calculation result for main program to use.
    

"""

def calculating_result(num1,operand1,num2,operand2,num3):
    if operand1 == '+' and operand2 == "-":
        result = num1 + num2 - num3
    elif operand1 == '-' and operand2 == "+":
        result = num1 - num2 + num3
    elif operand1 == '+' and operand2 == "*":
        result = num1 + num2 * num3
    elif operand1 == '*' and operand2 == "+":
        result = num1 * num2 + num3
    elif operand1 == '-' and operand2 == "*":
        result = num1 - num2 * num3
    elif operand1 == '*' and operand2 == "-":
        result = num1 * num2 - num3
    elif operand1 == '+' and operand2 == "+":
        result = num1 + num2 + num3
    elif operand1 == '-' and operand2 == "-":
        result = num1 - num2 - num3
    elif operand1 == '*' and operand2 == "*":
        result = num1 * num2 * num3
    else:
        result = None
    return result