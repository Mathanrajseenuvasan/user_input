class Person():
    data = []
    def __init__(self):
        self.register()
            
    def register(self):
        x = int(raw_input("< 1 > to register\n"))
        if x == 1:
            self.swt()
        else:
            print("Try again")
            self.register()
        
    def swt(self):
        
        for i in range(0, 1):
            self.dictionary = { 
                "name": raw_input("Enter name\n"),
                "age" : int(raw_input("Enter age\n"))
            }
            self.data.append(self.dictionary)
            self.stored()
            


    def stored(self):
        x = int(raw_input("< 1 > View \n< 2 > Register \n< 3 > Exit\n"))
        if x == 1:
            self.view()
        elif x == 2:
            self.swt()
        else:
            exit

    def view(self):
         print (self.data)
    
p1 = Person()

