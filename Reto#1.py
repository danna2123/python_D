print("Digite el codigo del producto")
codigo = input()
print("Digite el nombre del producto")
nombre = input()
print("Digite la cantidad comprada del producto")
c = float(input())
print("Digite el valor del producto")
v = float(input())
vt = v*c
vi = vt*0.19
vti = vt+vi
print("Código del producto es: ",codigo)
print("Nombre al producto es: ",nombre)
print("Valor unitario sin IVA es: ",vt)
print("El valor de la compra es: ",vti)



