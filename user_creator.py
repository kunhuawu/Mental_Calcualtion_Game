# -*- coding: utf-8 -*-
"""
Kunhua Wu
Date: 2020/12/19

Description of this program : 
    
    This program will be imported by the main program mental_calculation_game.
    
    This program will return Player class object based on user input data.
    This program will output password file and store it for future use.
    This program will also verify if existing user enter correct password.
    
    For all the attributes, password is private.

"""

import os

def user_build():
    
    class Player:
    
        def __init__(self, name, password = "", sign = "1",
                     highscore = 0, timescore = 0):
    
            self.name = name
            self.__password = password
            self.sign = sign
            self.highscore = highscore
            self.timescore = timescore
            
        def set_name(self, name):
            if name == "":
                return False
    
            self.name = name
            return True
        
        def set_password(self, password):
            if password == "":
                return False
    
            self.__password = password
            return True 
        
        def set_highscore(self, highscore):
            if highscore == "":
                return False        
    
            self.highscore = highscore
            return True 
        
        def set_timescore(self, timescore):
            if timescore == "":
                return False        
    
            self.timescore = timescore
            return True         
        
        def set_sign(self, sign):
            if sign == "":
                return False        
    
            self.sign = sign
            return True 
    
        def __repr__(self):
            description = "Hi, " + self.name + ". Your best score record is " \
                + str(self.highscore) + ". Your time mode record is beating " \
                + str(self.timescore) + " questions!"
            return description
    
        def __str__(self):
            description = "Hi, " + self.name + ". Your best score record is " \
                + str(self.highscore) + ". Your time mode record is beating " \
                + str(self.timescore) + " questions!"
            return description
        

    
    name_is_not_empty = False
    while name_is_not_empty == False:
        name_input = input("Please enter your name : ")
        if len(name_input) > 0:
            name_is_not_empty = True
        else:
            print("Invalid : Name can not be empty.")
            name_is_not_empty = False
        
    try :
        os.mkdir('./user/%s' % name_input)
        print("Welcome! New Player!")
        password_input = input("Please enter your password : ")        
        password_file = open('./user/%s/password.txt' % name_input, 'w')
        password_file.write(password_input)
        password_file.close()
        print("Your file saved")
        player1 = Player(name_input, password_input)
            
    except FileExistsError :
        password_to_enter = input("You played before. Please enter your"
                                  " password to login : " )
        password_file = open('./user/%s/password.txt' % name_input, 'r')
        password = password_file.read()
        password_file.close()
        password_valid = False
            
        while password_valid == False:
            if password_to_enter == password:
                password_valid = True
                sign = "1"
                print("Login success! Welcome back,", name_input)
            else:
                password_to_enter = input("Incorret password, please retry"
                                          " or enter Q to quit : ")
                if password_to_enter.upper() == "Q":
                    sign = "0"
                    password_valid = True
                    
        try :
            highscore_file = open('./user/%s/highscore.txt' % name_input, 'r')
            best_score = int(highscore_file.read())
            try:
                timescore_file = open('./user/%s/timescore.txt' \
                                      % name_input, 'r')
                time_score = int(timescore_file.read())
                player1 = Player(name_input, password_to_enter, sign)
                player1.set_highscore(best_score)
                player1.set_timescore(time_score)
                highscore_file.close()
                timescore_file.close()
            except FileNotFoundError:
                player1 = Player(name_input, password_to_enter, sign)
                player1.set_highscore(best_score)
                highscore_file.close()
        except FileNotFoundError:
            try:
                timescore_file = open('./user/%s/timescore.txt' \
                                      % name_input, 'r')
                time_score = int(timescore_file.read())
                player1 = Player(name_input, password_to_enter, sign)
                player1.set_timescore(time_score)
                timescore_file.close()
            except FileNotFoundError:
                player1 = Player(name_input, password_to_enter, sign)
            
    return player1
