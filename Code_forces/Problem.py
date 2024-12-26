# print is the if it's palindrom

result = "YES"
num = input()
reverse = num[::-1]

i = 0 
j = 0

while i<len(num) :
    if num[i] != reverse[i] :
        result = "NO"
    i+=1

while j<len(num) :
    if reverse[0]== "0" :
        result = "NO"
        reverse = reverse[1:]
    j+=1
    

print(reverse)
print(result)


