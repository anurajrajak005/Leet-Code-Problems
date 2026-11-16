# find the second largest element in a list without sorting
# li = [12,34,55,38]
# output = [38]

li = [12,34,55,38]
largest = 0
second_largest = 0

for i in li:
    if i > largest:
        second_largest = largest
        largest = i


    if i > second_largest and i<largest :
        second_largest = i
print(second_largest)
