i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

print("-------------------------")


for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break

print("-------------------------")

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)

#break and continue only operate on a single level of loop.
print("-------------------------")

def break_loop():
    for i in range(1, 5):
        if (i == 2):
            return(i)
        print(i)
    return(5)

def break_all():
    for j in range(1, 5):
        for i in range(1,4):
            if i*j == 6:
                return(i)
            print(i*j)

break_all()
"""
1 # 1*1
2 # 1*2
3 # 1*3
4 # 1*4
2 # 2*1
4 # 2*2
# return because 2*3 = 6, the remaining iterations of both loops are not executed
"""
print("-------------------------")
for i in [0, 1, 2, 3, 4]:
    print(i)

print("-------------------------")
for i in range(5):
    print(i)

print("-------------------------")
for i in range(1,4):
    print(i)

print("-------------------------")
for x in ['one', 'two', 'three', 'four']:
    print(x)

print("-------------------------")
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

print("-------------------------")
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key)