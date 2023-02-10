# conversão de tipos , coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro 
# tipos imutaveis e primitivos:
# str, int, float, bool

print('1', type('1'))


print(int('1') + 1)#vai converter e somar

print(int('1'), type(int('1'))) # coversão para int

print(float('1.2')+ 1)
print(type(float('1') + 1)) # coversão para float

print(bool(''))# coversão para bool
print(bool(' '))
print(bool('1 '))

print(str(11)+ 'B')# coversão para str
