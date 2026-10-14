def simple_intrest(principal, intrest, time):
    return (principal *intrest*time)/100

if__name___ == "__main__":
    p=int(input("enter principal amt"))
    i=float(input("enter intrest"))
    t=int(input("enter time in months"))

print("simple intrest is :",simple_intrest(p,i,t))