# *Define a garage collection that stores 3 cars (models), it’s known that double of same models came to garage,
# # print garage models
garage = ['bmw', 'suzuki', 'opel']
count = 0
while count != 2:
    car = input()
    if car in garage:
        print(car)
    else:
        print('bmw')
    count += 1

