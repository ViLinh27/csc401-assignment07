#hw7.py  Collaborator: Vi-Anh Nguyen Amy Moretti
class Volume:
    def __init__(self,vol=0):#look
        self.vol=vol
        self.set(vol)
    def __repr__(self):
        return "Volume({})".format(self.vol)
    def set(self,newVol):#set to whatever volume inputed
        if newVol>11:
            self.vol = 11
        elif newVol<0:
            self.vol = 0
        else:
            self.vol = newVol
    def get(self):
        return self.vol
    def up(self,goUp):
        self.goUp=goUp
        newVol = self.vol+goUp
        if newVol>11:
            self.vol=11
        else:
            self.vol = newVol
        
    def down(self,goDown):
        self.goDown=goDown
        newVol = self.vol-goDown
        if newVol<0:
            self.vol=0
        else:
            self.vol = newVol
    def __eq__(self,other):
        if self.vol==other:
            return True
        else:
            return False


def partyVolume(fILe):
    f = open(fILe,'r')
    ivol=f.readline()
    ovol = f.readlines()
    return ovol.split()

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw7TEST.py'))

