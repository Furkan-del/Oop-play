class Counter:
    def __init__(self,count):
        self.count=count

    def increase_count(self,x):
        if(self.count>0):
           self.count=self.count-x
        else:
            print("you cant use this attribute")


