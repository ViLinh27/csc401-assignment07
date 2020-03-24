#Queue_comp.py

#####hw qs ################

#clamping
'''
using max and min to clamp

>>> #clamping a value betweten
>>> #0 and 11
>>> 
>>> #long way
>>> x=15
>>> #want to y=x, but clamped bwetn0 and 11
>>> if x>11:
	y=11
elif x<0:
	y=0
else:
	y=x

	
>>> y
11
>>> 
>>> x=-5
>>> if x>11:
	y=11
elif x<0:
	y=0
else:
	y=x

	
>>> x
-5
>>> y
0
>>> #short way to clamp
>>> #using max and min
>>> x=15
>>> y=max(min(x,11),0)# can be written other way around
>>> x
15
>>> y
11
>>> x=-5
>>> y
11
>>> y=max(min(x,11),0)# can be written other way around
>>> y
0
>>> x=7
>>> y=max(min(x,11),0)# can be written other way around
>>> y
7
>>> #max and min are essentailly if and else statements
'''
#Volume
'''
>>>v = Volume() #default constructor
>>>v #repr is being called
Volume(0)
>>>v.set(15)
>>>v #clamp
Volume(11)
>>>v.get()
11
'''

#partyvolume and reading the file
'''
reading the file-read the first line, then the rest
>>> f = open('party2.txt')
>>> f.readline()
'5\n'
>>> lines = f.readlines()
>>> lines[:10]
['D 8.5\n', 'U 0.0\n', 'D 2.0\n', 'D 6.0\n', 'U 8.75\n', 'D 5.5\n', 'D 2.5\n', 'D 0.75\n', 'U 9.75\n', 'D 9.0\n']
>>> line=lines[0]
>>> line
'D 8.5\n'
>>> #slice the extra out is option 1
>>> #split is another
>>> line.split()
['D', '8.5']
>>> #works great
'''
#############"review"
'''
assignment (=) makes two names refer to same object. any modifications to one
variable affects the other as well
(because it is the same object


this is not an issue for immutable objects like strings.
only for mutable ones

>>> lst=[2,3,4]
>>> lst2=lst
>>> lst.append(5)
>>> lst


to make a coopy call constructor when making assignment, that builds a new
object
>>> lst=[2,3,4]
>>>lst2=lst
>>> lst2 = list(lst)#make a new list based on first list
>>> lst.append(5)
>>> lst2
[2, 3, 4]
>>> 
[2, 3, 4, 5]
>>> lst2
[2, 3, 4, 5]
>>> 
'''


####queue-compsoition
'''
Queue is a FIFO container
-first in first out

objects are enqueued(added) to the back of the queue and dequeued(removed)
from the front.

two implementations:
1)Queue_comp.py-composition
2)Queue_inherit.py-inheritance

'''
#Queue class is based on list class

#composition with list
#self HAS a list: self.q
#the list is self.q





####list is an attubute of self
class Queue:
    def __init__(self,lst=[]):
        #create a list
        #make sure you call list constructor
        #inside to guarantee new lsit
        self.q = list(lst) #allows q = Queue() to work

#write repr early!!!!!!!!!
    def __repr__(self):
        return "Queue({})".format(self.q)

    def enqueue(self,item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)#pop doens't return outside of the pop method itself
        #or
        item = self.q.pop(0)
        return item

    #indexing calls__getitem__
    #q[1]->Queue.__getitem__(q,1)
    def __getitem__(self,index):
        return self.q[index]


    #we don't want this but if we did,
    #we could uncomment it
    #q[1]=77->Queue.__setitem(q,1,77)
    #def __setitem__(self,index,item):
    #    self.q[index]=item

    #len(q)-> Queue.__len__(q)
    def __len__(self):
        return len(self.q)

    def __eq__(self,other):
        return self.q==other.q

    #amazing, get iteration for free! (with the __getitem__
    #in is also for free thanks to __Getitem__


    #q1 and q2 are Queues
    #q1+q2 ->Queue.__add__(q1,q2)
    def __add__(self,other):
        return Queue(self.q+other.q)







##########sets###############
'''
set like a list but items are unique-NO DUPLICATES and NOT ORDERED
or like a dictionary without vlaues...

a set is mutable but items inside should be immutable:

comment: to create an empty set: say set(), not{}

>>> #set
>>> s = {1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> s.add(9)
>>> s
{1, 2, 3, 4, 9}
>>> s.add(3)
>>> s
{1, 2, 3, 4, 9}
>>> s.remove(4)
>>> s
{1, 2, 3, 9}
>>> s.remove(4)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s.remove(4)
KeyError: 4
>>> #discard is simimilar to remove but doesn't cause error if item is not there
>>> s.discard(3)
>>> s
{1, 2, 9}
>>> s.discard(3)
>>> s
{1, 2, 9}
>>> #==doesn't depend on order
>>> {1,2}=={2,1}
True
>>> #empty set
>>> s = {}
>>> s.add(2)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s.add(2)
AttributeError: 'dict' object has no attribute 'add'
>>> #above creates empty dictionary(the s={})
>>> #to create empty set:
>>> s = set()
>>> s
set()
>>> s.add(2)
>>> s
{2}
>>> set([1,2,3,3,2,1,7])
{1, 2, 3, 7}
>>> s = set('apple')
>>> s
{'e', 'l', 'p', 'a'}
>>> #order based on hash order
>>> #you cant depend on order
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> #can iterate though
>>> #don't depend on order:
>>> for item in s:
	print(item)

	
e
l
p
a
>>> s
{'e', 'l', 'p', 'a'}
>>> s =={'a' ,'p','l','e'}
True
>>> s is {'a' ,'p','l','e'}
False
>>> #is means same object, == means content
>>> s =={'a' ,'p','p','l','e'}
True
>>> 
>>> 
>>> 


>>> 

>>> {[1,2],[3,4]}
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    {[1,2],[3,4]}
TypeError: unhashable type: 'list'
>>> 

'''



















