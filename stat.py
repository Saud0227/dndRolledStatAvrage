from random import randint
from time import sleep

total = 0
statUnit = {}
for i in range(3,19):
    statUnit[i] = 0

print(statUnit)
while True:
    try:
        if total >= 10000:
            raise KeyboardInterrupt
        vals = []
        for i in range(4):
            vals.append(randint(1,6))
        valSum = sum(vals)-min(vals)
        statUnit[valSum]+=1
        total+=1
        outStr = f'Total: {total}\n'
        for i in range(3,19):
            outStr += f'{i}: {round(statUnit[i]/total*100,2)}% '
        print(outStr)
        #sleep(0.01);
    except KeyboardInterrupt:
        print(statUnit)
        with open(f'{total}.txt', 'w') as f:
            f.write(str(statUnit))
            outStr = f'\nTotal: {total}\n'
            for i in range(3,19):
                outStr += f'{i}: {round(statUnit[i]/total*100,10)}%\n'
            f.write(outStr)

        break
