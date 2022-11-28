import random

def sort(a,l,r):
    #assert: a[l..r] is established    I
    i = l
    #INV: a[l..i-1] is sorted up, l <= i <= r+1   III
    while  (i <= r):
        p,j = i,i+1
        #INV: p such that a[p] <= a[i..j-1], i <= p <= j-1, i <= j <= r+1    V
        while (j <= r):
            if (a[j] < a[p]):
                    p = j
            j = j+1
        #assert: p such that a[p] <= a[i..r], i <= p <= r    IV
        a[p],a[i] = a[i],a[p]
        i= i+1
    #assert: a[l..r] is sorted up    II

N= 100
i = 0
a = []
while (i < N):
    a.append(random.randint(0,N-1))
    i = i+1
print(a)
sort(a,0,N-1)
print(a)