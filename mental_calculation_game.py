# -*- coding: utf-8 -*-
"""
Kunhua Wu
Date: 2020/12/19

Description of this program : 
    
    This is a mental calculation game.
    
    User will create a personal account and password for next login.
    User will receive 3 random number and 3 operand(+-*) to generate answers.
    For each calculation, only 2 operands are required, user need to verify.
    
    User can choose different game mode to play.
    Easy Mode : Quiz will be generated based on random number range 1 to 5.
    Hard Mode : Quiz will be generated based on random number range 1 to 10.
    Time Mode : User will have 60 seconds to keep answering quiz.
    
    In easy&hard mode, scores will be calculated and highest will be recorded.
    User can keep challenging themself to fight for higher score.
    
    In time mode, the number of correct answers will be recorded.
    User can keep challenging themself to fight for more correct asnwers.
    
    Have fun!

"""
from quiz_generator import quiz_build
from user_creator import user_build
from quiz_calculator import calculating_result
from folder_creator import create_user_folder
from random import randint
import time

def user_creator_assertion():
    assert user.name != "", "No user name is entered" 
def quiz_generator_assertion():
    assert len(quiz_to_take) != 0, "Quiz are not generated successfully" 
def quiz_calculator_assertion():
    assert user_result <= 729 and user_result >= -80, \
        "Impossible Calculation, check quiz data"
def folder_creator_assertion():
    assert isinstance(user, object) == True, \
        "User folder not created successfully" 

if __name__ == "__main__":
    
    create_user_folder() # user folder is created in this line
    user = user_build() # user object is created in this line
    user_creator_assertion() # test that at least user name is provided
    folder_creator_assertion() # test that user folder and subfolder are set.
    
    print(repr(user))
    
    user_build_success = False
    while user_build_success == False:
        if user.sign == "0":
            break
        else:
            user_build_success = True
            
        print("Which mode you want to play?")    
        
        answer = True
        
        while answer == True:
            level_choice_valid = False
            while level_choice_valid == False:
                level_choice = input("Enter 1 for easy, 2 for hard,"
                                     " 3 for Time Mode, Q to quit : ")
                if level_choice == "1":
                    level_choice_valid = True
                    quiz_type = randint(1,4)
                    quiz_to_take = quiz_build(1,6,1,quiz_type)
                    quiz_number = randint(0, 125)
                if level_choice == "2" or level_choice == "3":
                    level_choice_valid = True
                    quiz_type = randint(1,4)
                    quiz_to_take = quiz_build(1,10,1,quiz_type)
                    quiz_generator_assertion()#test quiz is generated properly.
                    quiz_number = randint(0, 728)                    
                if level_choice.upper() == "Q":
                    print("Thanks for playing, ", user.name)
                    break
                if level_choice not in "123":
                    level_choice_valid = False
                        
            if level_choice.upper() == "Q":
                break
        
            tStart = time.time()
            
            quiz = {'A':quiz_to_take[quiz_number][0], 
                    'B':quiz_to_take[quiz_number][1], 
                    'C':quiz_to_take[quiz_number][2], 
                    'D':'+', 
                    'E':'-',
                    'F':'*'}
                    
            print()        
            print("Hi, ", user.name)
            print()
            
            print("A is",quiz['A'])
            print("B is",quiz['B'])
            print("C is",quiz['C'])
            print("D is",quiz['D'])
            print("E is",quiz['E'])
            print("F is",quiz['F'])
                
            target_result = quiz_to_take[quiz_number][3]
            
            valid_input = False
            while valid_input == False:
                print("Target Number is : ", target_result)
                target_input = input("Enter the 5 characters sequence like"
                                     " ABCDE without seperator to generate"
                                     " %s or enter Q to quit:" % target_result)
                if target_input.upper() == "Q":
                    print("Thanks for playing, ", user.name)
                    break
                if len(target_input) == 5:
                    input_1st,input_2nd,input_3rd,input_4th,input_5th = \
                        list(target_input.upper())
                    if input_1st in "ABC" and input_3rd in "ABC" and \
                        input_5th in "ABC" and input_2nd in "DEF" and \
                            input_4th in "DEF" :
                            valid_input = True
                    else:
                        valid_input == False
                        print("Invalid input. Please try again.")
                        
                if len(target_input) != 5:
                    print("Invalid input. Please enter 5 characters.")
                    valid_input = False
            
            if target_input.upper() == "Q":
                break
        
            user_result = calculating_result(quiz[input_1st],quiz[input_2nd],
                                             quiz[input_3rd],quiz[input_4th],
                                             quiz[input_5th])
            quiz_calculator_assertion()#test the formula is correct
            print("Your calculate result is :", user_result)
            tEnd = time.time()
            
            correct_count = 0
            if level_choice == "3": #start to apply time mode
                time_left = round(60 - (tEnd - tStart),2)
                while time_left > 0:
                    if user_result == target_result:
                        correct_count += 1
                        print("Correct! GOGOGO NEXT~")
                        print("You got ", time_left, " seconds left." )
                    if user_result != target_result:
                        print("Wrong! Go next!!")
                        print("You got ", time_left, " seconds left." )
                        
                    level_choice_valid = True
                    quiz_type = randint(1,4)
                    quiz_to_take = quiz_build(1,10,1,quiz_type)
                    quiz_number = randint(0, 728)                    
            
                    quiz = {'A':quiz_to_take[quiz_number][0], 
                            'B':quiz_to_take[quiz_number][1], 
                            'C':quiz_to_take[quiz_number][2], 
                            'D':'+', 
                            'E':'-',
                            'F':'*'}
                    
                    print()        
                    print("Hi, ", user.name)
                    print()
                    
                    print("A is",quiz['A'])
                    print("B is",quiz['B'])
                    print("C is",quiz['C'])
                    print("D is",quiz['D'])
                    print("E is",quiz['E'])
                    print("F is",quiz['F'])
                
                    target_result = quiz_to_take[quiz_number][3]
            
                    valid_input = False
                    while valid_input == False:
                        print("Target Number is : ", target_result)
                        target_input = input("Enter the 5 characters sequence"
                                             " like ABCDE without seperator to"
                                             " generate %s or enter Q to quit:" 
                                             % target_result)
                        if target_input.upper() == "Q":
                            print("Thanks for playing, ", user.name)
                            break
                        if len(target_input) == 5:
                            input_1st,input_2nd,input_3rd,input_4th,input_5th \
                                = list(target_input.upper())
                            if input_1st in "ABC" and input_3rd in "ABC" \
                                and input_5th in "ABC" and input_2nd in "DEF" \
                                and input_4th in "DEF":
                                valid_input = True
                            else:
                                valid_input == False
                                print("Invalid input. Please try again.")
                                
                        if len(target_input) != 5:
                            print("Invalid input. Please enter 5 characters.")
                            valid_input = False        
            
                    if target_input.upper() == "Q":
                        break
        
                    user_result = calculating_result(quiz[input_1st],
                                                     quiz[input_2nd],
                                                     quiz[input_3rd],
                                                     quiz[input_4th],
                                                     quiz[input_5th])
                    quiz_calculator_assertion()#test the formula is correct
                    print("Your calculate result is :", user_result)
                    tNow = time.time()
                    time_left = round(60 - (tNow -tStart),2)
                    
                print("YOU BEAT", correct_count, "QUESTIONS THIS TIME!!" )
                
                if correct_count > user.timescore:
                    user.timescore = correct_count
                    timescore_file = open('./user/%s/timescore.txt' 
                                          % user.name, 'w')
                    timescore_file.write("%s\n" % str(user.timescore))
                    timescore_file.close()
                user_choice = input("Do you want to play it again ? (Y/N)")
                while user_choice.upper() not in "YN":
                    user_choice = input("Do you want to play it again ? (Y/N)")
                if user_choice.upper() == 'Y':
                    answer = True
                if user_choice.upper() == "N":
                    print("Thanks for playing, ", user.name)
                    break

                
            if level_choice == "1" or level_choice == "2": #easy&hard mode
                
                if user_result == target_result:
                    print("Great! You make the correct answer!")
                    if (tEnd - tStart < 10):
                        print("Your mental calculation is so fast!")
                    if (tEnd - tStart > 10):
                        print("However, you dont do it quick")
                else:
                    answer = False
                    print("Sorry~You made the wrong answer")
                    
                print()
                print("The seconds you spent is : ", round(tEnd - tStart, 2))
                
                if answer == True:
                    if level_choice == "1":
                        score = round(10000/(tEnd - tStart))
                    if level_choice == "2":
                        score = round(20000/(tEnd - tStart))
                    print("Your score is ", score)
                    if score > user.highscore:
                        user.highscore = score
                    print("Your highest score record ever is : ", 
                          user.highscore)
                    
                    new_score_file = open('./user/%s/highscore.txt' 
                                          % user.name, 'w')
                    new_score_file.write("%s\n" % str(user.highscore))
                    new_score_file.close()
                    
                    user_choice = input("Do you want to play it again ? (Y/N)")
                    while user_choice.upper() not in "YN":
                        user_choice = input("Do you want to play it again ?"
                                            " (Y/N)")
                    if user_choice.upper() == 'Y':
                        answer = True
                    if user_choice.upper() == "N":
                        print("Thanks for playing, ", user.name)
                        break
                    
                else:
                    print("You got no scores.")
                    user_choice = input("Do you want to play it again ? (Y/N)")
                    while user_choice.upper() not in "YN":
                        user_choice = input("Do you want to play it again ?"
                                            " (Y/N)")
                    if user_choice.upper() == 'Y':
                        answer = True
                    if user_choice.upper() == "N":
                        print("Thanks for playing, ", user.name)
                        break
                