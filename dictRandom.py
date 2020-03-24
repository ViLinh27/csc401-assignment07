# dictRandom.py

##### week 7 #####

# loose ends - while
# hw q's
# dict/tuple/set(?)
# random
# hand back midterm

##### hw q's #####
'''
>>> primeFac(90)
[2,3,3,5]
>>> primeFac(13)
[13]

accumulate list of factors
n = 90
facs = []
potfac = 2

observe that 2 divides 90, so perform div
n = 45
facs = [2]
potfac = 2

observe 2 does NOT divide 90, so increment
potfac:
n = 45
facs = [2]
potfac = 3

3 divides 45, so do it
n = 15
facs = [2,3]
potfac = 3

3 divides 15, so do it
n = 5
facs = [2,3,3]
potfac = 3

3 does not divide 5, increment potfac
n=5
facs = [2,3,3]
potfac = 4

4 does not divide 15, increment potfac
n=5
facs = [2,3,3]
potfac = 5

5 does divide 5, so do it
n = 1
facs = [2,3,3,5]
potfac = 5

STOP because n == 1

start with n=n,potfac=2,facs=[]

while number not factored
(i..e, while ...)

    if potfac is a factor
    perform divisioon
        divide n by potfac
        add potfac to facs

    otherwise (not a factor)
        increment potfac
'''

# sublist
'''
>>> sublist([1,2,3],[5,1,4,2,5,3,9])
True
>>> sublist([1,2,1],[5,1,4,2,5,3,9])
False
>>> sublist([1,2,1],[5,1,1,2,7])
False

i=0 # counter for first list
j=0 # counter for second list

while i and j are still in range

    if first list at position i
    matches second at position j

        increment both counters

    otherwise (not a match)

        increment j

when the loop ends one or both
of i and j are out range

if i is out of range
means you found all the matches
so return True

otherwise (j is out of range and
i is not), so return False
'''

##### dict(ionary) #####

'''
dict
- {key:val, key:val, ...}
- {} empty dictionary
- container for key: val paris
  like a list, but indexed by keys
- insertion ordered
- dictionaries are mutable
- keys must be immutable (hashable)
- keys must be unique

operators
- d[key] returns corresponding value
- d[key]=value  sets key:value

- in, not in - work on keys
  applies to containment and iteration (for)

methods
- pop(key) deletes pair and returns value
(.values(),.items(),.keys(), .update())


  



suppose that we want to write a phone
book application.  Given a name, we want
to retrive corresponding phone number.

how do we store the data?

names = ['frank','sue','sally']
numbers = [333,222,666]

or

phonenums = [ ('frank',333), ('sue',222), ...]

but there is something much better!

>>> # dict
>>> phonenums = {'frank':333, 'sue':222, 'sally':777}
>>> phonenums
{'frank': 333, 'sue': 222, 'sally': 777}
>>> # retrieve items by key
>>> phonenums['sue']
222
>>> # can also assign
>>> phonenums['fred'] = 111
>>> phonenums
{'frank': 333, 'sue': 222, 'sally': 777, 'fred': 111}
>>> # can change a value
>>> phonenums['sally']=666
>>> # can change a value
>>> phonenums
{'frank': 333, 'sue': 222, 'sally': 666, 'fred': 111}
>>> # cant change a key!
>>> # to capitalize sue, remove and reassign
>>> phonenums.pop('sue')
222
>>> phonenums
{'frank': 333, 'sally': 666, 'fred': 111}
>>> phonenums['Sue'] = 222
>>> phonenums
{'frank': 333, 'sally': 666, 'fred': 111, 'Sue': 222}
>>> [1,2]==[2,1]
False
>>> {'a':1,'b':2} == {'b':2,'a':1}
True
>>> # in works on keys
>>> 'frank' in phonenums
True
>>> 222 in phonenums
False
>>> for key in phonenums:
	print(key, phonenums[key] )

	
frank 333
sally 666
fred 111
Sue 222
>>> # to get ordered
>>> for key in sorted(phonenums):
	print(key, phonenums[key] )

	
Sue 222
frank 333
fred 111
sally 666
>>> sorted(phonenums)
['Sue', 'frank', 'fred', 'sally']
>>> 
>>> # slight detour
>>> lst = [5,2,3]
>>> lst.sort()
>>> lst = [5,2,3]
>>> lst2 = lst.sort()
>>> lst2
>>> lst
[2, 3, 5]
>>> lst = [5,2,3]
>>> lst2 = sorted( lst )
>>> lst2
[2, 3, 5]
>>> lst
[5, 2, 3]
>>> 
>>> # back on track
>>> phonenums
{'frank': 333, 'sally': 666, 'fred': 111, 'Sue': 222}
>>> phonenums[ ['Curie','Marie'] ] = 888
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    phonenums[ ['Curie','Marie'] ] = 888
TypeError: unhashable type: 'list'
>>> # use a tuple instead
>>> phonenums[ ('Curie','Marie') ] = 888
>>> phonenums
{'frank': 333, 'sally': 666, 'fred': 111, 'Sue': 222, ('Curie', 'Marie'): 888}
>>> hash( ('Curie', 'Marie') )
492658831
>>> hash( 492658831 )
492658831
>>> hash( 20934809230498238 )
473209328
>>> 

'''

##### tuple #####
'''
tuple
- (item,item,item,...)
- like a list but immutable
- can be used as dict keys

>>> # tuple
>>> t = (4,2,3)
>>> t[1]
2
>>> len(t)
3
>>> t.sort()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> sorted( t )
[2, 3, 4]
>>> t
(4, 2, 3)
>>> t[1]=1
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    t[1]=1
TypeError: 'tuple' object does not support item assignment
>>> # tuple assignment
>>> a,b = 2,3
>>> a
2
>>> b
3
>>> t
(4, 2, 3)
>>> x,y,z = t
>>> x
4
>>> y
2
>>> z
3
>>>
>>> # most languages, need temp variable
>>> # to swap
>>> # in python
>>> a,b = 2,3
>>> a,b = b,a
>>> a,b
(3, 2)
>>> 
'''

##### list comprehension #####
'''
not in the book but incredibly useful

>>> # list comprehension
>>> range(5)
range(0, 5)
>>> list( range(5) )
[0, 1, 2, 3, 4]
>>> [i*i for i in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [i*i for i in range(10) if i%3!=0]
[1, 4, 16, 25, 49, 64]
>>> # can do similar things with tuples, dictionaries
>>> 
'''

##### random #####

'''
random
- module for generating (pseudo)
  random numbers

import random

functions
- randrange(start,stop) - int drawn
  from range(start,stop)
- randrange(n) - int drawn from
  range(n)
- choice(sequence) - random item from
  sequence

- uniform(start,stop) - float
- sample(sequence,n) - n item sample from
  sequence
- shuffle(sequence) - shuffles sequence
  in place (mutable)
- seed(n) - seeds random generator


>>> import random
>>> random
<module 'random' from 'C:\\Python\\lib\\random.py'>
>>> # random integers
>>> random.randrange(3)
0
>>> random.randrange(3)
1
>>> random.randrange(3)
2
>>> random.randrange(3)
1
>>> random.randrange(3)
1
>>> random.randrange(3)
1
>>> [ random.randrange(3) for i in range(20)]
[1, 1, 2, 0, 2, 0, 1, 0, 0, 2, 1, 2, 2, 2, 0, 1, 0, 2, 0, 2]
>>> # die roll
>>> [ random.randrange(1,7) for i in range(20)]
[3, 4, 5, 1, 3, 4, 3, 5, 6, 2, 5, 4, 4, 5, 3, 1, 5, 1, 1, 6]
>>> # coin flip
>>> random.randrange(2)
1
>>> random.randrange(2)
0
>>> # random floats
>>> [ random.uniform(0,1) for i in range(10)]
[0.6118970848141451, 0.8280632784038988, 0.3331351372890984, 0.7302785763532248, 0.7036425461655201, 0.06298427426119957, 0.9170189691149498, 0.2217038962141865, 0.8033450541462023, 0.14249439390882446]
>>> 
>>> # we will use
>>> random.choice( [1,'apple',7] )
7
>>> random.choice( [1,'apple',7] )
'apple'
>>> random.choice( [1,'apple',7] )
1
>>> # coin flips
>>> [ random.choice('HT') for i in range(10)]
['H', 'T', 'T', 'H', 'T', 'T', 'H', 'T', 'H', 'T']
>>> 
>>> # dont need probably
>>> random.sample( range(10), 5 )
[7, 1, 6, 2, 4]
>>> lst = list(range(10))
>>> lst
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> random.shuffle( lst )
>>> lst
[9, 8, 5, 7, 0, 6, 1, 2, 4, 3]
>>> random.sample( range(10), 11 )
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    random.sample( range(10), 11 )
  File "C:\Python\lib\random.py", line 321, in sample
    raise ValueError("Sample larger than population or is negative")
ValueError: Sample larger than population or is negative
>>> random.shuffle('abc')
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    random.shuffle('abc')
  File "C:\Python\lib\random.py", line 278, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> # detour
>>> a,b = 2,3
>>> # swap
>>> a = b
>>> b = a
>>> a
3
>>> b
3
>>> 
>>> # random seeding
>>> random.seed(0)
>>> [random.choice('HT') for i in range(10)]
['T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'H']
>>> [random.choice('HT') for i in range(10)]
['H', 'T', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'T']
>>> random.seed(0)
>>> [random.choice('HT') for i in range(10)]
['T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'H']
>>> 
'''

##### random example #####
'''
make this work: simulate a dice game
where you roll 2 dice, keep rolling as
long as you get doubles. return the total
number of pips rolled:

e.g.
3 3
5 5
2 1

return 19

>>> diceTotal() # for above simul
19
'''

import random

# while, accumulator
def diceTotal(): # no parameters

    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    pips = die1 + die2
    #print( die1, die2 )
    while die1==die2:
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        #print( die1, die2 )
        pips += die1 + die2
    return pips
    
'''
>>> diceTotal()
18
>>> [diceTotal() for i in range(30)]
[7, 3, 5, 6, 9, 4, 10, 6, 7, 11, 10, 6, 7, 11, 9, 8, 3, 10, 9, 10, 7, 7, 6, 14, 6, 7, 8, 8, 10, 10]
>>>
'''

'''
make this work:
>>> frequencies( [5,8,5,8,5,7] )
{5:3, 8:2, 7:1}
'''

def frequencies( lst ):
    ''' return a dictionary with frequency
counts of the items in lst '''

    # create an empty dict
    counts = {}
    # iterate over the lst
    for item in lst:
        # if item is NEW add
        # to dict with count of 1
        if item not in counts:
            counts[item]=1
        # if OLD, add 1 to its count
        else:
            counts[item]+=1
    # return dict
    return counts

'''
>>> frequencies( [5,8,5,8,5,7] )
{5: 3, 8: 2, 7: 1}
>>> lst = [random.randrange(10) for i in range(1000)]
>>> frequencies( lst )
{2: 98, 4: 97, 6: 90, 0: 105, 9: 105, 5: 101, 1: 94, 7: 126, 3: 90, 8: 94}
>>> frequencies( [diceTotal() for i in range(10000)] )
{10: 651, 9: 1229, 3: 583, 5: 1118, 7: 1666, 11: 715, 6: 1148, 4: 530, 8: 1113, 20: 55, 15: 156, 18: 96, 21: 70, 13: 139, 12: 95, 19: 110, 14: 81, 17: 139, 33: 3, 16: 122, 30: 4, 29: 7, 23: 49, 32: 2, 27: 14, 22: 33, 43: 2, 26: 11, 28: 10, 24: 8, 31: 7, 25: 23, 41: 2, 35: 2, 40: 2, 49: 1, 36: 2, 39: 1, 46: 1}
>>> frequencies( 'abracadabra')
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
>>> f = frequencies( [diceTotal() for i in range(10000)] )
>>> for k in sorted(f):
	print( k, f[k])

	
3 562
4 545
5 1105
6 1114
...
'''

'''
make this work:
encode will translate any
characters found in the dictionary
(and leave others alone)

>>> d = {'a':'k', 'b':'g'}
>>> encode( 'bat', d )
'gkt'

'''

def encode( word, d ):

    # accumulate a str
    ans = ""
    # iterate over word
    for letter in word:
        # if letter is in dictionary
        # replace it
        if letter in d:
            ans += d[letter]
        # otherwise use original letter
        else:
            ans += letter
    return ans

'''
>>> d = {'a':'k', 'b':'g'}
>>> encode( 'bat', d )
'gkt'
>>>
'''























