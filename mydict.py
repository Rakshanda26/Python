class Dict_function :
    def __init__(self,a):
        self.a = a
        
    def verify_dict(self):
        if type(self.a) != dict:
            raise Exception(self.a , 'is not a dictionary')
        return 1
    
    
    def get_keys(self):
        if self.verify_dict():
            return list(self.a.keys())
        
    def get_values(self):
        if self.verify_dict():
            return list(self.a.values())
        
        
    def user_input(self):
        b = eval(input())
        self.a.update(b)
        return self.a,
    
    def insertion(self,**kwargs):
        for k , v in kwargs.items():
            self.a[k] = v
        return self.a
            
            