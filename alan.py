t=0.0
x=0.0
dx=0.0000001
while x <=2.0:
    t=t+(-2*x**3+3*x**2-2*x)*dx
    x=x+dx

print ('alan=',t)
