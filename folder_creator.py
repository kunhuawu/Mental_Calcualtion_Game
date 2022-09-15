# -*- coding: utf-8 -*-
"""
Kunhua Wu
Date: 2020/12/19

Description of this program : 
    
    This program will be imported by the main program mental_calculation_game.
    
    This program will create the "user" folder at the current directory.
    The "user" folder will be used to store output user data.
    
    This program will run 1 time only.

"""
import os

def create_user_folder():
    try :
        os.mkdir('user')
    except :
        pass
