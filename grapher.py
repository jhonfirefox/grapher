#Ajuste No lineal para una funcion senoidal
#Programa para series de datos con python
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time as tm

#Funcion para convertir string a float, devueve un lista np
def str2float(lst):
	return np.array([float(i) for i in lst])

#Funcion para contar el numero de datos por columna
#Si encuentra espacio vaio, el programa no lo cuenta
#como dato numerico
def size_Num(array):
	n2 = array.size
	n3 = 0
	
	for i in range(0,n2):
	   if array[i] != '':
	      n3 += 1
	return n3

#Se pide el nombre de archivo 
print("====Programa para graficar un conjunto de datos====")
print("Nombre de archivo de los datos con extension: ", end="")
name = str(input())

print("Delimitador de campo para ambos archivos: ", end="")
delimiter = str(input())

print("# de linea de inicio de datos de ambos archivos: ", end="")
sLine = int(input())

print("Potencia de escala, eje x: ", end="")
xScale = int(input())

print("Numero de conjunto de datos a graficar: ", end="")
numAdjust = int(input())

fileData = np.loadtxt(name,dtype=str, delimiter=delimiter, skiprows = sLine)

labels = ["Etiqueta 1", "Etiqueta 2", "...."]

plt.figure()
j = 0
rand.seed(tm.time())
for i in range(0,2*numAdjust-1,2):
	n = size_Num(fileData[:,i])
	x_exp = str2float(fileData[:n,i])
	y_exp = str2float(fileData[:n,i+1])
	#x_exp = (x_exp - x_exp[0])*10**(xScale)
	
	#color for graphs
	r = rand.random()
	g = rand.random()
	b = rand.random()
	#plt.figure()
	plt.plot(x_exp,y_exp, "-", label = "Exp.Data_"+str(int(1+(i/2))), color=(r,g,b))
	#plt.plot(x_exp,y_exp, "-", label = labels[i/2], color=(r,g,b))

plt.xlabel("x_data(Unit)")
plt.ylabel("y_data(Unit)")
plt.title("Title1")
plt.legend()
#plt.savefig("grapher_"+str(int(rand.random()*10))+".png")
plt.savefig("grapher_0.png")
plt.show()
