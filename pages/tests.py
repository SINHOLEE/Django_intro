from django.test import TestCase
import random
# Create your tests here.
real_lotto = [21, 25, 30, 32, 40, 42]
laa = [21, 25, 30, 32, 40, 42]
 # 희원이가 랜덤으로 뽑은 로또
count = 0
get = ''
while get != 'get':
    count += 1
    sum = 0
    for i in range(len(real_lotto)):
        if real_lotto[i] == sorted(list(random.sample(range(1,46), 6)))[i]:
            sum += 1
    if sum == 6:
        get = 'get'
    print(count, sum, sorted(list(random.sample(range(1,46), 6))))
    
print('당첨', count)