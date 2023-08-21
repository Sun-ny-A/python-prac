#question1
#Write a function to print "hello_USERNAME!" 
#USERNAME is the input of the function. 
#The first line of the code has been defined 
#as def hello_name(user_name)

def hello_name(user_name):
    return "Hello " + user_name

user_name = input("What is your name? ")
print(hello_name(user_name))


#question2
#Write a python function first_odds 
#that prints the odd numbers from 1-100 
#and returns nothing def first_odds()

range (1,101)
def first_odd():
    for i in range(1,101):
        if i %2 !=0:
            print(i)


#question3
#Write a Python function max_num_in_list 
#to return the max number of a given list. 
#The first line of the code has been defined 
#as def max_num_in_list(a_list)

def max_num_in_list(a_list):
    max = a_list
    for i in a_list:
        if i > max:
            return max


#question4
#Write a function to return 
#if the given year is a leap year. 
#A leap year is divisible by 4, 
#but not divisible by 100 unless 
#it is also divisible by 400. 
#The return should be boolean Type (true/false). 
#def is_leap_year(a_year):

def is_leap_year(a_year):
    if(a_year % 4== 0):
        return True
    elif a_year % 100 == 0 and a_year % 400 ==0:
        return True
    else:
        return False
    

#question5
#Write a function to check to see if 
#all numbers in the list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, 
#but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type. 
#def is_consecutive(a_list):

def is_consecutive(a_list):
    if i in range(len(a_list)):

    #I'm not really sure how to do this problem at all.
    #I think I have to create a loop sequence
    #that checks if the previous number, a, +1 
    #is equal to b and so forth...but what does that
    #look like?