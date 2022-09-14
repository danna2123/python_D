n = int(input("ingrese la cantidad de productos: "))

codigo = []
nombre = []
cantidad = []
precio = []
iva = []

for i in range(n):
    codigo.append(input("Digite el codigo: "))
    nombre.append(input("Digite el nombre del producto: " ))
    cantidad.append(float(input("Digite la cantidad del producto: " )))
    precio.append(float(input("Digite el valor del producto: " )))
    iva.append(int(input("Tipo de IVA:\n1: Exento de IVA\n2: Bienes, donde se aplica como IVA el 5%\n3: General, donde se aplica como IVA el 19% : \n" )))
"""print(len(codigo))
print(len(nombre))
print(len(cantidad))
print(len(precio))
print(len(iva))"""
total_pro = []
valor_iva = []
iv = []
total_compra = []
total_venta = 0
total_iva = 0
for i in range(n):
    total_pro.append(cantidad[i] * precio[i])
    if iva[i]==1:
        iv.append(0)
        valor_iva.append(total_pro[i])
    elif iva[i]==2:
        iv.append(total_pro[i] * 0.05)
        valor_iva.append(total_pro[i] + iv[i])
    elif iva[i]==3:
        iv.append(total_pro[i] * 0.19)
        valor_iva.append(total_pro[i] + iv[i])
    total_venta += valor_iva[i]
    total_iva += iv[i]
for i in range(len(nombre)):
    compras=[]
    compras.append(nombre[i])
    compras.append(codigo[i])
    compras.append(total_pro[i])
    compras.append(valor_iva[i])
    total_compra.append(compras[:])

ordenado=sorted(total_compra,key=lambda x: x[0])

for compras in ordenado:
    print(compras[1])
    print(compras[0])
    print(compras[2])
    print(compras[3])
print(total_venta)
print(total_iva)

