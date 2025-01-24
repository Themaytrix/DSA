import random
class Add():
    def __init__(self):
        self.arr = []
        self.dic = {}
        
    def add_sth(self,val):
        if val in self.arr:
            return 
        index = len(self.arr)
        print(index)
        
    
    
    def remove_sth(self,val):
        if val not in self.arr:
            return 
        
        
        
    def getRandom(self):
        return random.choice(self.arr)
    

sth = Add()

print(sth.dic)