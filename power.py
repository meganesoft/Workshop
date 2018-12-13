N = int(input())

total = max([pow(p,N) for p in range(1,5)])

print(total)

def Base_four(X,n):
    if (int(X/n)):
        return Base_four(int(X/n),n)+str(X%n)
    return str(X%n)

x4 = Base_four(total,4)
print(x4)
