import matplotlib.pyplot as plt 
import sympy as sp 

x= sp.Symbol('x')


n1 = int(input('Ingrese el primer coeficiente de x: '))
exp1 = int(input('Ingrese el primer exponente de x: '))

f = (n1*x**exp1)

f1=(exp1*n1*x**(exp1-1))


print(f'La función es:  {f}')
print(f'La derivada de {f} es {f1}')


sp.plot(f,f1)
