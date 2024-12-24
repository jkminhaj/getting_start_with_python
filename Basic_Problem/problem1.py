# Take 3 numbers from user and find the largest value

num1 = input()
num2 = input()
num3 = input()

if num1 > num2 and num1 > num3 :
    print(f"{num1} is largest")
elif num2 > num3 :
    print(f"{num2} is largest")
else :
    print(f"{num3} is largest")