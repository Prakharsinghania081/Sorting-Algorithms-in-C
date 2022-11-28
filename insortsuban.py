import random


def insort(a,l,r):
    #assert: a[l..r] is established    I
    i = l
    #INV: a[l..i-1] is sorted up, l <= i <= r+1   III
    while  (i <= r):
        x,j = a[i],i
        #INV: (x <= a[j+1..i]), i >= j >= l
        while (j > l) and (a[j-1] > x):
            a[j] = a[j-1]
            j = j-1
        #assert: ((j=l) or x > a[j-1]) and (x <= a[j+1..i])
        a[j] = x
        i= i+1
    #assert: a[l..r] is sorted up    II

N= 100
i = 0
a = []
while (i < N):
    a.append(random.randint(0,N-1))
    i = i+1
print(a)
insort(a,0,N-1)
print(a)