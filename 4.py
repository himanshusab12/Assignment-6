class Pangram:
    def __init__(self,l):
        self.l=l
    def create_l(self): 
        for a in range(0,26):
            l.append(chr(97+a))
    def calc(self):
        a = input("Enter a string")
        for x in a:
            if x in l:
                l.remove(x)
        if len(l)==0:
            print("It is a pangram")
        else:
            print("Not a pangram")
l=[]
panG = Pangram(l)
panG.create_l()
panG.calc()
