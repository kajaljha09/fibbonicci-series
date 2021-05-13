def fac1():

    if n==1:
        return 1
    else:
        return n*fac1(n-1)
"""def fac2():
   
    fac2=1
    for i in range(n):
        fac2=fac2*i+1
    return fac2"""

n=int(input("Enter the no u want to calculate factorial for"))
fac1(n)

