# -*- coding: utf-8 -*-
"""
Kunhua Wu
Date: 2020/12/19

Description of this program : 
    
    This program will be imported by the main program mental_calculation_game.
    
    This program will return quiz list based on user input data.
    Different kinds of quiz will be generated.
    The main program will randomly pick up quiz from this return list.

    type 1 : + -
    type 2 : - +
    type 3 : + *
    type 4 : - *

"""


def quiz_build(a,b,c,d):
    
    A = range(a,b,c)
    
    simple_result_type1_list = []
    for n1 in A:
        for n2 in A:
            for n3 in A:
                result = n1 + n2 - n3
                result_formula = "{} + {} - {} = {}".format(n1, n2, n3, result)
                simple_result_type1_list.append([n1, n2, n3, result, 
                                                 result_formula])
                
    simple_result_type2_list = []
    for n1 in A:
        for n2 in A:
            for n3 in A:
                result = n1 - n2 + n3
                result_formula = "{} - {} + {} = {}".format(n1, n2, n3, result)
                simple_result_type2_list.append([n1, n2, n3, result, 
                                                 result_formula])
    
    simple_result_type3_list = []
    for n1 in A:
        for n2 in A:
            for n3 in A:
                result = n1 + n2 * n3
                result_formula = "{} + {} * {} = {}".format(n1, n2, n3, result)
                simple_result_type3_list.append([n1, n2, n3, result, 
                                                 result_formula])
    
    simple_result_type4_list = []
    for n1 in A:
        for n2 in A:
            for n3 in A:
                result = n1 - n2 * n3
                result_formula = "{} - {} * {} = {}".format(n1, n2, n3, result)
                simple_result_type4_list.append([n1, n2, n3, result, 
                                                 result_formula])
                
                
    if d == 1:
        return simple_result_type1_list
    if d == 2:
        return simple_result_type2_list
    if d == 3:
        return simple_result_type3_list
    if d == 4:
        return simple_result_type4_list



                