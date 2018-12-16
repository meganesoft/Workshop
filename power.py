from collections import Counter
import re

N = int(input())
total = max([pow(p,N) for p in range(1,5)])

print(total)

def Base_four(X,n):
    if (int(X/n)):
        return Base_four(int(X/n),n)+str(X%n)
    return str(X%n)

def count_three(x: str) -> int:
    cnt = 0
    for word in re.finditer('3',x):
        cnt += 1
    return cnt

x4 = [str(Base_four(t,4)) for t in range(total)]
x4= ','.join(x4)
print(count_three(x4))
#print(count_three(x4))
