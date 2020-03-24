# reviewAndWhile.py

##### tonight #####

# midterm next week
# quizzes
# hw q's
# review
# while

##### midterm #####
'''
inclass students - 10/16 usual
classroom time.  we wont hold
class afterwards.

online students - please register
at DePaul campus or with proctor

can bring one double sided page
of notes (or 2 single sided)
HARDCOPY notes (will be collected)

two parts:
1) multiple choice (like quiz questions)
2) programming (like hw, but on paper.
   make sure your indentation is clear)

to study:
1) review quizzes (questions may look
   similar but be different)
2) solve problems from book/hw/ etc.
3) see midtermPractice.py in
   week 5 notes
'''

##### go over quizzes #####

'''
q1,#9 - off the record, but, or
returns the first "non-trivial/non-zero"
expression

>>> # in Python can be used for more than just booleans!
>>> 0 or 0 or 0 or 4
4
>>> x = 2
>>> y = 2
>>> y==1 or 3
3
>>> y=1 or 3
>>> y
1
>>> None or None or [1,2] or None
[1, 2]
>>>
'''

##### hw q's #####
'''
# 5.26 - rps
hint: dont use a loop

>>> rps('R','S') # player 1 wins
-1
>>> rps( 'P','S') # player 2 wins
1
>>> rps( 'S','S') # tie
0

def rps(p1,p2):

    if/elif/else - how many cases?
    3 or 9

hints:

p1='R', p2='S'

1) what is p1+p2?   'RS'

2)

>>> y==1 or y==3 or y ==5
True
>>> y in [1,3,5]
True
>>>

3) ['RS','SP', 'PR']

'''

# 5.39 - exclamation
'''
hint: dont use replace ! (can
actually make this work)

>>> exclamation('moon')
'moooooooon!'

0) iterate over the word
>>> exclamation('moon')
m
o
o
n

1) detect vowels and multiply them
>>> exclamation('moon')
m
oooo
oooo
n

2) accumulate that stuff
>>> exclamation('moon')
m
moooo
moooooooo
moooooooon

add ! and return

'''
##### review #####
'''
two ways to iterate

1)
>>> s = 'apple'
>>> for c in s:
	print( c )

	
a
p
p
l
e

2)
>>> # indexed iteration
>>> s = 'apple'
>>> for i in range(len(s)):
	print(i,s[i])

	
0 a
1 p
2 p
3 l
4 e
>>> 

(there is a 3rd way, too)
>>> # off the record
>>> # enumerate
>>> s = 'apple'
>>> enumerate(s)
<enumerate object at 0x03B0B558>
>>> list( enumerate(s) )
[(0, 'a'), (1, 'p'), (2, 'p'), (3, 'l'), (4, 'e')]
>>> for i,c in enumerate(s):
	print( i,c )

	
0 a
1 p
2 p
3 l
4 e
>>>
'''

# accumulation
'''
4 step process:
0) print version first
1) initialize an accumulator before loop
2) accumulate in loop
3) return after the loop

'''

# search
'''
for
    if
        return
return
'''

# practice

def f(s):
    x=0
    for i in range(len(s)):
        if s[i]==s[i].upper():
            x+=i
    return x
'''
>>> f('abcABC')
12
>>> f('HowAREYou')
18

sum of the indices of
capital letters!

'''

def g(nums):
    answer = []
    for num in nums:
        if num%2==0:
            answer.append( num )
    return answer

'''
>>> g( range(0,100,5) )
[0,10,20,30,...,90]
>>> g( range(0,100,7) )
[0,14,28,42,56,70,84,98]
'''

def h(s):
    n=0
    m=0
    for c in s:
        if c not in 'aeiou':
            n+=1
            m = max(m,n)
        else:
            n = 0
    return m
'''
n = # consecutive consonants
    during iteration
m = maximum of all n values seen

>>> h('fight')
>>> h('bottle')
>>> h('mississippi')
'''

'''
is the given list of numbers
always non-decreasing (i.e., either
increasing or constant/level)

>>> isSorted([2,3,3,4,5,7,9,10] )
True
>>> isSorted([2,3,3,4,5,2,7,9,10] )
False

this is a SEARCH for a consecutive
pair that decreases.  If you find
such a pair, return False, otherwise
return True after the loop.

need indexed iteration in order to
look at pairs.

'''

def isSorted( numlst ):

    for i in range(len(numlst)-1):
        # if pair is decreasing
        if numlst[i] > numlst[i+1]:
            #print( i, numlst[i], numlst[i+1] )
            return False
    return True

'''
>>> acronym('Federal Bureau Investigation')
'FBI'
>>> acronym('national security agency')
'NSA'
'''

def acronym( phrase ):
    
    acro = ""
    # iterate over words
    for word in phrase.split():
        acro+=word[0]
    return acro.upper()

##### while #####
# wont cover on midterm!

'''
while <bool expression>:
    <body>
<rest of your code>

while
- like a repeating if statement
- continues to execute the body
  until the boolean expression is
  False, then continue with rest
  of the program
- more general purpose

use a for loop if you can, but
you may have to use a while loop
if you dont know ahead of time
what you are going to iterate
over

body of the loop may execute
0,1,2,... infinite number of times

important: condition should become
False at some point (or have another
way of stopping the loop)

loop modifiers, apply to for loops as well:

return - terminates function, hence all loops
break - terminates innermost loop
continue - terminates current iteration, continues
           with next iteration
pass - does nothing

'''

'''
want this to work:
>>> pigLatin('apple')
'appleay'
>>> pigLatin('pear')
'earpay'

>>> pigLatin('string')
'ingstray'
'''

# v1 - only handles one consonant 
def pigLatin( word ):

    # if consonant move it to the back
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    # always add 'ay'
    return word + 'ay'

# v2 - handles up to 3 (or n) consonants
# using n if statements,
# not ideal!
def pigLatin( word ):

    # if consonant move it to the back
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    # always add 'ay'
    return word + 'ay'

# v3 - handles any number of consonants
def pigLatin( word ):

    # if consonant move it to the back
    while word[0] not in 'aeiou':
        word = word[1:] + word[0]
    # always add 'ay'
    return word + 'ay'

'''
>>> pigLatin('string')
'ingstray'
>>> pigLatin('zmrzlina')
'inazmrzlay'
>>>

>>> pigLatin('by')  # Ctrl-c to stop!
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    pigLatin('by')
  File "C:/Users/esedgwic/Documents/CSC401_Sedgwick/reviewAndWhile.py", line 358, in pigLatin
    word = word[1:] + word[0]
KeyboardInterrupt
>>> 
'''

def d(n):
    n = abs(n)
    c = 0
    while n>0:
        n//=10  # n = n//10
        c+=1
    return c

'''
>>> d(165)
???
>>> d(123456789)
???
'''

##### user input using while #####

'''
make this work:
>>> sumUserNums()
Enter a number: 12
Enter a number: 9
Enter a number: 3.3
Enter a number:
24.3
>>>
'''

# accumulator, while

##### loop and a half pattern #####

def sumUserNums():

    total = 0
    ans = input('Enter a number: ') # either a number or ''
    while ans!='':
        total += eval(ans)
        ans = input('Enter a number: ') # either a number or ''
    return total

##### infinite loop pattern #####

def sumUserNums():

    total = 0
    while True:
        ans = input('Enter a number: ')
        if ans=='':
            break
        else:
            total += eval(ans)
    return total


##### rewriting loop as a while #####

'''
while loop is more general than
a for loop.  every for loop can
be rewritten as a while.

>>> s = 'abc'
>>> for c in s:
	print( c )

	
a
b
c
>>> for i in range(len(s)):
	print(i, s[i])

	
0 a
1 b
2 c
>>> # rewrite as a while
>>> s
'abc'
>>> i = 0
>>> while i<len(s):
	print(i,s[i])
	i+=1

	
0 a
1 b
2 c
>>> 
'''





    














