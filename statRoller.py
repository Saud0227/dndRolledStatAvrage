from random import randint
from time import sleep

total = 0

for j in range(6):

    vals = []
    for i in range(4):
        vals.append(randint(1,6))
    valSum = sum(vals)-min(vals)
    print(valSum)
    #sleep(0.01);
