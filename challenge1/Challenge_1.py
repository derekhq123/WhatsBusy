
# coding: utf-8

# In[1]:


class MoneyBox:
    number_of_coins=0
    capacity=0
    def __init__(self, capacity):
        self.capacity=capacity


    def can_add(self, v):
        
        if self.number_of_coins+v<=self.capacity:
            
            return True
        else:
            return False
    def add(self, v):
        
        if self.can_add(v):
            self.number_of_coins+=v
        

