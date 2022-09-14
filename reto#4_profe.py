def ordenamiento_burbuja(N,codigo,cantidad,valor_unitario,iva,nombre,valor_producto,valor_final):
    for i in range(0,N-1):
        for j in range(i+1,N):
            if nombre[i]>nombre[j]:
                t=codigo[i]
                codigo[i]=codigo[j]
                codigo[j]=t
                t=nombre[i]
                nombre[i]=nombre[j]
                nombre[j]=t
                t=cantidad[i]
                cantidad[i]=cantidad[j]
                cantidad[j]=t
                t=valor_unitario[i]
                valor_unitario[i]=valor_unitario[j]
                valor_unitario[j]=t
                t=iva[i]
                iva[i]=iva[j]
                iva[j]=t
                t=valor_producto[i]
                valor_producto[i]=valor_producto[j]
                valor_producto[j]=t
                t=valor_final[i]
                valor_final[i]=valor_final[j]
                valor_final[j]=t
    return codigo,nombre,cantidad,valor_unitario,iva,valor_producto,valor_final
N=int(input())
total_ventas=0
total_iva=0
codigo=[]
nombre=[]
cantidad=[]
valor_unitario=[]
tipo=[]
valor_producto=[]
iva=[]
valor_final=[]
for i in range(N):
    codigo.append(int(input()))
    nombre.append(input())
    cantidad.append(float(input()))
    valor_unitario.append(float(input()))
    tipo.append(int(input()))
for i in range(N):
    valor_producto.append(cantidad[i]*valor_unitario[i])
    if tipo[i]==1:
        iva.append(0)
    elif tipo[i]==2:
        iva.append(valor_producto[i]*0.05)
    else:
        iva.append(valor_producto[i]*0.19)
    valor_final.append(valor_producto[i]+iva[i])
    total_iva+=iva[i]
    total_ventas+=valor_final[i]
codigo,nombre,cantidad,valor_unitario,iva,valor_producto,valor_final=ordenamiento_burbuja(N,codigo,nombre,cantidad,valor_unitario,iva,valor_producto,valor_final)
for i in range(N):
    print(codigo[i])
    print(nombre[i])
    print(valor_producto[i])
    print(valor_final[i])
print(total_ventas)
print(total_iva)
