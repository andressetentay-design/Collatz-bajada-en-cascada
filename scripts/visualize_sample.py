import math
import matplotlib.pyplot as plt

# simple Collatz step
def T(n):
    return 3*n+1 if n%2 else n//2

# compute signature until first value < 2**k
def first_drop_signature(n,k):
    A,B=0,0
    start = n
    limit = 2**k
    while n>=limit:
        if n%2:
            n = 3*n+1
            A += 1
        else:
            n = n//2
            B += 1
        # safety
        if A+B>10000:
            break
    return A,B,n

def sample_signatures(k,low_exp=10,high_exp=12):
    low = 2**low_exp
    high = 2**high_exp
    P_list=[]
    for n in range(low,high):
        A,B,_ = first_drop_signature(n,k)
        P_list.append(A+B)
    return P_list

if __name__=='__main__':
    k=10
    P = sample_signatures(k,10,12)
    plt.hist(P,bins=range(min(P),max(P)+2),edgecolor='black')
    plt.title('Distribution of P=A+B for sample [2^10,2^12)')
    plt.xlabel('P = A+B')
    plt.ylabel('Count')
    plt.show()
