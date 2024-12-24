# Taking input and storing on a variable
name = input()
# Or you can pass string for a good ux 
age = input("please input age : ")

sec_age = input("second age : ")

print("sum of age : ", age + sec_age)

"""
please input age : 20
second age : 20
sum of age :  2020 
"""

age_int = int(age) 
sec_age_int = int(sec_age)

# sum of int of ages :  40

print("sum of int of ages : ", age_int + sec_age_int);

#Note : the default type of input is string . here the age is string 