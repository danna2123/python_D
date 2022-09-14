def mover(lista,pos):
    v = lista[pos]
    j = pos
    while j>0 and v<lista[j-1]:
        lista[j] = lista[j-1]
    lista[j] = v

def ordenar(codigos,cantidad,tiva): # Burbuja
    for i in range(len(codigos)-1):
        if codigos[i+1] < codigos[i]:
            mover(codigos,i+1)
            mover(cantidad, i+1)
            mover(tiva, i+1)
            print(print)
            
nombre = {1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios = {1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

n = int(input(""))

codigos = []
cantidad = []
tiva = []
valores = []
ivas = []
valivas = []
t_valores = 0
t_iva = 0
for i in range(n):
    codigos.append(int(input("")))
    cantidad.append(float(input("")))
    tiva.append(int(input("")))

ordenar(codigos,cantidad,tiva)

for i in range(len(codigos)):
    valor = cantidad[i] * precios[codigos[i]]
    valores.append(valor)
    if tiva[i] == 1:
        iva = valor * 0
    elif tiva[i] == 2:
        iva = valor * 0.05
    else:
        iva = valor * 0.19
    ivas.append(iva)
    valivas.append(valor+iva)
    t_iva += iva
    t_valores += valor + iva
    print(codigos[i])
    print(nombre[codigos[i]])
    print(valores[i])
    print(valivas[i])
print(t_valores)
print(t_iva)
