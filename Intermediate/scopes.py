# global variable
balance = 1000 

def demo():
    # local scope 
    # here you can only get the value of any global variable 
    # can't modify the global variable 

    # local variable
    balance = 500
    # this balance is only for this function

    global balance # after using global you can modify the global variable