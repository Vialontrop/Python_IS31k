import random,os
from datetime import datetime
nums=[random.randint(1,100) for _ in range(5)]
with open('numbers.txt','w') as f:
    f.write('Date: '+str(datetime.now())+'\n')
    f.write('Numbers: '+str(nums))
print(os.path.exists('numbers.txt'))
with open('numbers.txt') as f:
    print(f.read())