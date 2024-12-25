# index   :0   1   2   3   4   5
numbers = [34 ,53 ,23 ,53 ,12 ,54]
# index   :-6  -5  -4  -3  -2  -1

# here numbers[0] and numbers[-6] is same

#  list   [start : end : steps] 

print(numbers[0:5]) # [34 ,53 ,23 ,53 ,12]

print(numbers[2:5]) # [23 ,53 ,12]

print(numbers[2:5]) # [23 ,53 ,12]


print(numbers[0:5:1]) # [34 ,53 ,23 ,53 ,12 ,54]
print(numbers[0:5:2]) # [34 ,23 ,12]

# reverse flow
print(numbers[5:2:-1]) #[54,12,53]
print(numbers[5:2:-2]) #[54,53]

print(numbers[0:]) # index 0 to end
print(numbers[:2]) # index start to until the position
print(numbers[:]) # start to end
print(numbers[::-1]) # reverse the list




