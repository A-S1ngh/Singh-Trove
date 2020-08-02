class Sandwich: #This is creating a class, which is a template for an object
    def __init__(self, bread, cheese, meat): #An object takes parameters, namely the self parameter, which refers to itself.
        self.bread = bread
        self.cheese = cheese
        self.meat = meat

    def lister(self):
        print(f"This sandwich has {self.bread}, {self.cheese}, and {self.meat}")

ham = Sandwich("rye", "cheddar", "ham")
print(ham.bread)
ham.lister()

def bruh():
    print("Bruh")

def decorator(function):
    print("I am running")
    function()
    print("I am finished")

decorator(bruh)
