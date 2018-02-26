'''
Integral hesaplama
'''
import sympy as sm
x=sm.Symbol('x')
f='2*x**2+3*x-1'
integral=sm.integrate(f,x)
alan=sm.integrate(f,(x,0,2))
print('f(x)=',f)
print('belirsiz integral I(x)=',integral)
print ('belirli integral=',alan)
