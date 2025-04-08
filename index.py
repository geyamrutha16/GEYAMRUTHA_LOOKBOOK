n = 5
num = 1
for i in range(n):
    for j in range(i+1):
        print(num,end = " ")
        num = num + 2
    print()

'''
n = int(input("Enter number of houses : "))
l = input("Enter food contained in each house : ").split(",")
l = [int(i) for i in l]
m = int(input("Enter number of rats : "))
unit = int(input("Food consumed by each rat : "))
f_unit = m * unit
food = 0

#approch 1
for i in range(len(l)):
    food = food + l[i]
    if food >= f_unit:
        print("All Rats consumed food")
        break

if food < f_unit:
    print((m - (food//unit)), "rats were left")

#approach 2
food = sum(l)
if food < f_unit:
    print((m - (food//unit)), "rats were left")
else:
    print("All Rats consumed food")

for i in range(len(l)):
    food = food + l[i]
    if food >= unit:
        print(i+1)
        break

if food < unit:
    print("Food is Deficient")
'''
