class Pascal_triangle:
    def __init__(self,l):
        self.l=l
    def calc(self): 
        for a in range(0,10):
            for b in range(0,a+1):
                if(b==0 or b==a):
                    l[a].append(1)
                else:
                    l[a].append(l[a-1][b-1]+l[a-1][b])
        return l
    def show(self):
        for a in range(0,10):
            if (a<10):
                print(' '*(9-a),end='')
            for b in range(0,a+1):
                print(l[a][b],end=' ')
            print()
l = [[],[],[],[],[],[],[],[],[],[]]
pasc = Pascal_triangle(l)
l=pasc.calc()
pasc.show()
