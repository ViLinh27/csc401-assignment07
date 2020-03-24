#Queue_inherit.py

####inheriit#########3

#MyList class inherits/subclasses/ is a child class of list
#an inherited class inheriits all fhe functionality of parent class
# but you can add

class MyList(list):#MyList inheriits from list

    # get rid of spaces in repr
    #override the repr method
    def __repr__(self):
        ans = "["
        for item in self:
            ans+=repr(item)+","
        return ans[:-1] + "]"
    #new methods
    def apply(self,f):
        for i in range(len(self)):
            self[i] = f(self[i])


            




