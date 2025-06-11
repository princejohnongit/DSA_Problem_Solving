import random as rd
class RandomizedSet:
    
    def __init__(self):
        self.store=[]
        self.val_to_index={}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index: 
            return False
        self.store.append(val)
        self.val_to_index[val]=len(self.store)-1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.store: 
            return False
        index_to_remove=self.val_to_index[val]
        last_element=self.store[-1]
        self.store[index_to_remove]=last_element
        self.val_to_index[last_element]=index_to_remove
        self.store.pop()
        del self.val_to_index[val]
        return True
        

    def getRandom(self) -> int:
        if self.store:
             return rd.choice(self.store)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
