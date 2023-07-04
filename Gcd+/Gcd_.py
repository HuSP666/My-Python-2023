a=int(input("1:"))
b=int(input("2:"))
m=max(a,b)
n=min(a,b)
r=m%n
while (r!=0):
    m=n
    n=r
    r=m%n
print("{}ºÍ{}".format(n,int(a*b/n)))