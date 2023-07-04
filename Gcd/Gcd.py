a=int(input("数字1是:"))
b=int(input("数字2是:"))
m=max(a,b)
n=min(a,b)
r=m%n
while (r!=0):
    m=n
    n=r
    r=m%n
print("{}和{}".format(n,int(a*b/n)))