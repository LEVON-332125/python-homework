# *Define collection of numbers, get number at random position if it doesn’t exceed some inputed threshold value
import random
numbers=[22,232,34,445,511,612,77789]
clock=random.randint(0,len(numbers))
print(clock)
# print(len(numbers))
# print(numbers[clock])
if numbers[clock]>int(input()):
    print(numbers[clock])
else:
    print(clock)
