import sympy as sm
x=sm.Symbol('x')
f='x**2+1'
turev=sm.diff(f,x)
print('f(x)=',f)
print('dy/dx=',turev)


