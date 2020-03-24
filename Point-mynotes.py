#Point.py


#####hw.py#########

#simul
'''
simulate n games of rps
and decide who won more, player 1, player 2, or tie

>>>simul(10000)
Player 1
'''
#copy your rps() from hw3.py
def rps(p1,p2):
    #your code here
    #returns either -1,0,1
    pass
#future reference:
#from hw3 import rps


'''
def simul(n):#accumulator
    #easier to use a for loop
    #counter loop useful
    #don't need i in loop
    for: #repeat n times
        p1= choose RPS randomly
        p2 = choose RPS randomly
        rps(p1,p2)#should be inside the function
'''
#made up example:
#game called doubles, roll once
#win if you get doubles(return 1)
#and lose otherwise(return 0)
#want to simulate playing n rounds of this game

#function to play one round
import random
def doubles():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    if d1==d2:#win
        return 1
    else:#lose
        return 0

#run simulation of n games of doubles
'''
>>>simulate(10000)
.16 # won 16% of the time
'''
#model for testCraps()/simul()
def simulate(n):
    wins = 0
    for i in range(n):
        result = doubles()
        if result==1:
            wins+=1
    return wins/n


#a little slicker:
def simulate(n):
    wins=0
    for i in range(n):
        wins+=doubles()
    return wins/n

#for the minimalist
def simulate(n):
    return sum([doubles() for i in range(n)!])/n
    
#don't call funcition obring Pam as needed Iim

#craps
'''simulate single game of craps and retun1 if player wins and 0 if player loss.
initital roll win if roll total is 7 or 11
lose if you get2,3,12

otherwise roll until win if you repeat initial roll
lose if you roll a 7

rules for win or lose is different for initial roll than for subsequencet rolls


initial rol before loop
quit(return) if you win or lose/otherwise....
make sure you remember your first roll(store it somehwere)

while
    keep rolling dice and check if you win or lose.

#looks like:
if
    return something
elif
    return somtihng

    while
        if
            return 1
        elif:
            return 0
'''
  

#######object oreiented progrmaming###############
# we will write our own classes(types)
#IMPORTANT slight of haNd###########
'''
when you have an aboject
obj = Myclass()
and you call a method
ob.method(arg1,arg3....)
slmost always,a ctually python exectues the foliwng
MyClass.method(obj.arg1 arg2

exapmlsd:

'''
#contructor calls make a copy of an object when called




# method is function(def) defined uinside  A CLASS.

#####Point Cass!########3

#v1-everythig is expliity
'''make this work
>>>p = Ponit(x0
'''

class Point:
    pass

# think of get method as a conversion method
#inside class always call first parameter self
#modifies are assignment statements
#gets are return statements

#p.move(1,1)=> Point.move(p,1,1)

# in general object gets data
#class gets method


#methods with _(underscores) run
#automaticaly but you don't have a choice of the name of the method

#__init__ makes sure to have defaults so any code that needed to be there
#to begin with is already there.
##is a constructor
#resposonbivle for initializing object(primarily to add needed attributes)

#list(var) makes a new object out of var

#fstrings are succint formatted strings
#take everything literally except for things in {}

#if is is true == is true but not vise versa






























