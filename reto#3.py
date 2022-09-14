n = int(input("Ingrese la cantidad de productos: "))
lista_producto = []
producto = {"codigo": "","nombre": "","cantidad":0,"precio":0,"iva":0}
for i in range(n):
    producto["codigo"]=input("digite el codigo: ")
    producto["nombre"]=input("Digite el nombre del producto: " )
    producto["cantidad"]=float(input("Digite la cantidad del producto: " ))
    producto["precio"]=float(input("Digite el valor del producto: " ))
    producto["iva"]= int(input("Tipo de IVA:\n1: Exento de IVA\n2: Bienes, donde se aplica como IVA el 5%\n3: General, donde se aplica como IVA el 19% : \n" ))
    lista_producto.append( producto.copy())
#for i in range(5):
#    print (n)
total_venta=0
total_iva=0
for indice in range(n):
    total_pro = lista_producto[indice]["cantidad"]*lista_producto[indice]["precio"]
    if lista_producto[indice]["iva"]==1:
       iv = 0
       valor_iva = total_pro+iv
    elif lista_producto[indice]["iva"]==2:
        iv = total_pro*0.05
        valor_iva = total_pro+iv
    else:
        iv = total_pro*0.19
        valor_iva = total_pro+iv
    total_venta += valor_iva
    total_iva += iv

misProductos=[]

for i in range(len(producto)):
    productos=[]
    productos.append(producto[codigo])
    productos.append(producto[nombre])
    productos.append(producto[cantidad])
    productos.append(producto[precio])
    productos.append(producto[iva])
    misProductos.append(producto[:])
print(misProductos)
    
ordenado=sorted(misProducto,key=lambda x: x[0])

for producto in ordenado:
    print(lista_producto[indice]["codigo"])
    print(lista_producto[indice]["nombre"])
    print (total_pro)
    print (valor_iva)
print(total_venta)
print(total_iva)
