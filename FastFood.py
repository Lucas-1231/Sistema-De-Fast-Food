print('1. Hambúrguer-R$10,00')
print('2. Batata frita-R$5,00')
print('3. sorvete-R$4,00')
print('4. refrigerante-R$3,00')

item = input('qual intem você deseja?')
quant = int(input('quantos você deseja?'))

if item == '1':
    print("valor total: R$", 10 * quant)
    print('tempo estimado 10 minutos')
if item == '2':
    print("valor total: R$", 5 * quant)
    print('tempo estimado 10 minutos')
if item == '3':
    print("valor total: R$", 4 * quant)
    print('tempo estimado 10 minutos')
if item == '4':
    print("valor total: R$", 3 * quant)
    print('tempo estimado 10 minutos')
input()