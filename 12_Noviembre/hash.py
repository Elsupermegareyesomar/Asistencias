def formaArreglo(tama�o):
	T=[None]*tama�o
	return T
def obtenerLlaveNumerica(llave):
	hash=0
	mul=1
	for char in str(llave):
    	hash+=mul*ord(char)
    	mul+=1
	return hash
def H(llaveN):
	return llaveN%13
def hashLineal(llave_hash,tama�o,T):
	for j in range(1,tama�o+1):
    	nuevoIndice=(llave_hash+j)%13
    	if(nuevoIndice==len(T)):
        	nuevoIndice=-1
        	break
    	else:
        	if T[nuevoIndice] is None:
            	break
        	else:
            	nuevoIndice=-1
	return nuevoIndice
def agregar(llave,valor,T,tama�o):
	indiceTabla=H(obtenerLlaveNumerica(llave))
	print("\nEl �ndice es:",indiceTabla)
	ParllaveValor=[llave,valor]
	if T[indiceTabla] is None:
    	T[indiceTabla]=list([ParllaveValor])
    	return True
	else:
    	for par in T[indiceTabla]:
        	if par[0]==llave:
            	par[1]=valor
            	return true
    	indiceTabla=hashLineal(indiceTabla,tama�o,T)
    	print("El nuevo �ndice es:",indiceTabla)
    	if indiceTabla!=-1:
        	T[indiceTabla]=list([ParllaveValor])
        	return True
    	else:
        	print("Tabla llena",indiceTabla)
        	
def buscar(llave,tama�o,T):
	indiceTabla=H(obtenerLlaveNumerica(llave))
	print(indiceTabla)
	if T[indiceTabla] is not None:
    	for par in T[indiceTabla]:
        	if par[0]==llave:
            	return par[1]
        	else:
            	for j in range(indiceTabla,tama�o):
                	nuevoIndice=(indiceTabla+j)%13
                	for par1 in T[nuevoIndice]:
                    	if par1[0]==llave:
                        	return par1[1]
	return None
Tabla=formaArreglo(13);
agregar("Hola9",12213239,Tabla,13)
print(Tabla)
agregar("Hola4",12213234,Tabla,13)
print(Tabla)
agregar("Hola1",12213231,Tabla,13)
print(Tabla)
agregar("Hola2",12213232,Tabla,13)
print(Tabla)
agregar("Hola3",12213233,Tabla,13)
print(Tabla)
agregar("Hola5",12213245,Tabla,13)
print(Tabla)
agregar("Hola6",12213236,Tabla,13)
print(Tabla)
agregar("Hola7",12213237,Tabla,13)
print(Tabla)
agregar("Hola8",12213238,Tabla,13)
print(Tabla)
agregar("Hola10",12213210,Tabla,13)
print(Tabla)
agregar("Hola11",122132511,Tabla,13)
print(Tabla)
agregar("Hola12",122132512,Tabla,13)
print(Tabla)
agregar("Hola13",122132513,Tabla,13)
print(Tabla)