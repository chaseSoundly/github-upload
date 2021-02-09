########## IMPORTS ##########
import random
import math
import time
#############################

########## CLASSES ##########
class test():
    def __init__(self):
        self.score = 0
        self.num = 10
        
    def mc(self, q, a, b, c, d, ca):
        print(q)
        print("a. " + a)
        print("b. " + b)
        print("c. " + c)
        print("d. " + d)
        
        answer = input()
        
        if (answer == ca):
            print_delay("You are correct! Good job!\n")
            self.score = self.score + 1
        else:
            print_delay("Sorry, that was incorrect.\n")
            
    def tf(self, q, ca):
        print(q + " t or f?")
        
        answer = input()
        
        if (answer == ca):
            print_delay("You are correct! Good job!\n")
            self.score = self.score + 1
        else:
            print_delay("Sorry, that was incorrect.\n")
    
    def calc_score(self):
        self.score = (self.score/self.num)*100
        print("Your score:", end = " ")
        print(self.score)
#############################

########## FUNCTIONS ##########
# Print Delay Function
# Input: Message to print, Optional time for delay
# Output: No return
# Prints a message with delay after
def print_delay(m, t = 2):
    print(m)
    time.sleep(t)
###############################

########## SUBMAIN ##########
# Copyright Function to display copyright
def cr():
    print("---- Python Fun ----")
    print("December 10, 2020")
    print("By Chase Scott")
    print("© 2020")
    print("--------------------\n")

# Go function to contain program
def go():
    t = test()
    print_delay("Welcome to Christmas Trivia!")
    t.mc("How many wise men were there?", "1", "4", "2", "3", "d")
    t.mc("What were the gifts of the wise men?",
         "Silver, Gold, Myrrh", "Frankincense, Gold, Sweet Incense",
         "Frankincense, Gold, Myrrh", "Silver, Gold, Bronze", "c")
    t.mc("What does nativity stand for?", "Outcast", "New", "Born", "Baby", "c")
    t.tf("We know Jesus was born in a stable.", "f")
    t.mc("Who was the first person to create the nativity scene (statues)?",
         "Saint Benedict", "Saint Francis of Assisi", "Pope Honorius III",
         "Saint Bernadette", "b")
    t.tf("King Herod ordered all babies under the \nage of one to be killed.", "f")
    t.mc("How many babies were killed during the massascre?", "100-200", "50-100", "30-50", "7-20", "d")
    t.mc("What was the probable age of Mary when she gave birth to Jesus?",
         "12-14 years old", "15-18 years old", "19-22 year old", "23-25 years old", "a")
    t.mc("When was the first Christmas song made?", "336", "714", "250", "115", "a")
    t.tf("Joseph and Mary most likely had an arranged marriage.", "t")
    t.calc_score()
    print("Thanks for playing!")
#############################

########## MAIN ##########
# Main function to start program
def main():
    cr()
    go()
##########################

main()