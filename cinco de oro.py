import random
set = {0}
while len(set) < 6:
    for i in range(5):
        num = random.randrange(1, 49)
    set.add(num)  
set.remove(0)
print(set)
print("Vamos tu puedes")
print("Una vez mas")