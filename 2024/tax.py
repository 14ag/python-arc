n=float(input("the"))
if n<=85528:
    t=0.18*n-556.02
elif n>=85528:
    t=14839.02+0.32*(n-85528)
if t<0: t=0
t= round(t,0)
print("The tax is:", t, "thalers")
