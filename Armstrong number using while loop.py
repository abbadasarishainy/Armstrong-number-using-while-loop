def armstrong(x):
    n=x
    org=n
    p=len(str(n))
    s=0
    while n!=0:
        d=n%10
        s=s+d**p
        n=n//10
    if s==org:
        print("Arm strong number")
    else:
        print("not a armstrong")
s=int(input())
armstrong(s)
