N = int(input("Digite N, la cantidad de productos a procesar\n" ))
totalcom = 0
sumiva = 0
for i in range(N):
    codigo = input("Digite el codigo del producto \n" )
    nombre = input("Digite el nombre del producto \n" )
    can = float(input("Digite la cantidad comprada del producto \n" ))
    val = float(input("Digite el valor del producto \n" ))
    iva = int(input("Tipo de IVA:\n1: Exento de IVA\n2: Bienes, donde se aplica como IVA el 5%\n3: General, donde se aplica como IVA el 19% : \n" ))
    vt = val*can
    if iva==1:
        iva = 0
        pivat = vt+iva
    elif iva==2:
        iva = vt*0.05
        pivat = vt+iva
    else:
        iva = vt*0.19
        pivat = vt+iva     
    totalcom = totalcom + iva
    sumiva = sumiva + pivat
    print(codigo)
    print(nombre)
    print(vt)
    print(pivat)
print(sumiva)
print(totalcom)
