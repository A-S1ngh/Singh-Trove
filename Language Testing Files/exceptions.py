try:
    print(x) #This brings up - NameError: name 'x' is not defined
except NameError:
    print("Error!: X is not defined")
except:
    print("Something else went wrong")
