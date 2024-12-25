# if the func is void then it will return none

# def = define 
def doubleIt (num1 ,  num2 ):
    return num1 * num2

# optional parameter  : num3 is optional parametere . others are required
def sum (num1 , num2 , num3=0 ):
    return num1 + num2 + num3 

# args = arguments 
def sum (*nums):
    return nums  # reutuns a "tuple" which is kinda array  (2,3,5)

# Unordered parameter pass
def full_name (first, last):
    return first +" "+ last 

full_name(last="Islam",first="Minhajul")

# kargs = key with argumetns
def full_name (first, last , **kargs):
    print(kargs) # will return an object 

    for key , value in kargs.items():
        print(key+" "+value)

full_name(last="Islam",first="Minhajul",title="Developer")

# multiple return form function

def calculator ( num1 , num2 ):

    sum = num1 + num2
    min = num1 - num2
    div = num1 / num2
    mul = num1 * num2

    # return [sum , min , div , mul ]  return as array 
    
    return sum , min , div , mul # will return a tuple by default 