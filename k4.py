class Cub():
    def __init__(self, state=[1,1,1,1,1,1,1,1]):
        self.state = state
       
    def makeU(self):
        self.state = self.state[-2:] + self.state[:-2]
       
    def makeU2(self):
        self.makeU()
        self.makeU()
       
    def makeUprime(self):
        self.makeU2()
        self.makeU()
       
    def flipEdge(self, edgeState, doFlip):
        return (edgeState*2%2) if doFlip else edgeState
   
    def flipMultiple(self, indexes):
        self.state = [self.flipEdge(self.state[idx], idx in indexes) for idx in range(len(self.state))]
   
    def makeAdjFlipNear(self):
        self.flipMultiple([3,4])
        self.state = [self.state[n] for n in [0,3,2,4,1,5,6,7]]
       
    def makeAdjFlipAway(self):
        self.flipMultiple([5,2])
        self.state = [self.state[n] for n in [2,1,5,3,4,0,6,7]]
       
    def makeOppFlip(self):
        self.flipMultiple([1,4])
        self.state = [self.state[n] for n in [0,4,2,1,3,5,6,7]]
   
    def get_state(self):
        return self.state

#this need to be fixed...
def removeSymmetries(cases):
    output = []
    for c in cases:
        l = []
        i = list(c[:])
        for n in range(4):
            i.insert(0, i.pop())
            i.insert(0, i.pop())
            l.append(''.join(map(str,i[:])))
        output.append('-'.join(sorted(l)))
    return [list(i.split('-')[0]) for i in list(set(output))]

def main():
    ellCases = []
   
    cub = Cub()
    flips = [cub.makeAdjFlipNear, cub.makeOppFlip, cub.makeAdjFlipAway]
    aufs = [cub.makeU, cub.makeU2, cub.makeUprime]
   
    for a in aufs*10:
        a()
        ellCases.append(cub.get_state())
        for f in flips*10:
            f()
            ellCases.append(cub.get_state())
               
    print(len(ellCases))
    print(len(removeSymmetries(ellCases)))
   
main()
input()