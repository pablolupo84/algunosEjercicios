#Hola Julia, aca te paso todo el tp, fijate cualquier cosa escribime
#Hoy ya no voy a estar conectado, epro escribime a mi email pablolupo84@gmail.com
#o a mi whastapp 1131997473...te lo envio por workana cualquier cosa hablamos
#tene en cuenta que realice pruebas y modifique algunos de los valroes del main
#asi que si queres ajustalos y verifica, si encontras algo avisame

def minimo(x,y):
	menor=x
	if menor>y:
		menor=y
	return menor

def minimo_3(x,y,z):
	w = minimo(x,y)
	return  minimo(w,z)

def contar_pares(l):
	pares=0
	for elemento in l:
		if elemento%2==0:
			pares+=1
	#si la lista es vacia retorno 0
	return pares

def posicion_minimo_lista(l):
	contador=0
	pos_min=0
	minimo=l[pos_min]
	for elemento in l:
		if(elemento<minimo):
			minimo=elemento
			pos_min=contador
		contador+=1
	#si la lista es vacia retorno 0
	return pos_min

def media(l):
	sumatoria=0
	longitud=0
	resultado=0
	for elemento in l:
		sumatoria+=elemento
		longitud+=1
	#si la lista es no vacia -> evito dividir por cero
	if longitud!=0:
		resultado = (sumatoria/longitud)
	return resultado

def reverso(l):
	l_invertida=l[::-1]
	return l_invertida

def es_capicua(l):
	l_invertida=reverso(l)
	if l==l_invertida:
		return True
	else:
		return False
	
def concatenar(l1,l2):
	return l1 + l2

def sumar_listas(l1,l2):
	#Asumimos igual longitud y no vacias
	lista_suma=l1
	i=0
	for elemento2 in l2:
		lista_suma[i]=lista_suma[i]+elemento2
		i+=1
	return lista_suma

def quitar_apariciones(l,elem):
	while elem in l:
            l.remove(elem)
	return l

def ordenar_lista(l):
	for dato in range(len(l)-1,0,-1):
		for item in range(dato):
		# Si el elemento de la posición i+1 está desordenado respecto
		# al de la posición i, reubicarlo dentro del segmento (0:i]
			if l[item+1]< l[item]:
				aux=l[item+1]
				l[item+1]=l[item]
				l[item]=aux
	return l

def fibo_recursiva(n):
	if n == 0: #para n=0 es 0
		return 0
	if n == 1: #para n=1 es 1
		return 1
	return fibo_recursiva(n-1) + fibo_recursiva(n-2)


def fibo_iterativa(n):
	a = 1
	b = 0
	for i in range(n):
		c = b+a
		a = b
		b = c
		# a, b = b, a + b -> esta es otra de forma de escribir lo de arriba
	return b

def main():

	# En el main les proveemos algunas pruebas basicas para las funciones del TP
	# Estan originalmente comentadas para que puedan ejecutar el codigo de forma gradual.
	# La sugerencia respecto a la ejecucion es la siguiente.
	# 1. Decidir la funcion a implementar (ejemplo: minimo).
	# 2. Implementarla.
	# 3. Venir al main, y buscar los casos de test correspondietes.
	# 4. Descomentar las lineas correspondientes y probar la ejecucion.
	# 5. En caso de encontrar errores, tratar de corregirlos hasta que la implementacion sea correcta.
	# 6. Opcionalmente, agregar casos de prueba que consideren necesarios.
	# 7. Pasar a la siguiente funcion.
	a = 4
	b = 3
	c = 2
	l1 = [1,6,3]
	l2 = [7,5,6]
	l3 = ['a','b','b','a','b']
	l4 = [6,2,3,16,9,3,13,4,1]
	elem = 5
	n = 10

	# test minimo.
	# descomentar las siguientes dos lineas
	print('minimo: ', minimo(a,b))
	print('minimo: ', minimo_3(a,b,c))

	# test contar_pares
	# descomentar las siguientes dos lineas
	print('contar_pares: ', contar_pares(l1))
	print('contar_pares: ', contar_pares(l2))

	# test posicion_minimo_lista
	# descomentar las siguientes dos lineas
	print('min_lista: ', posicion_minimo_lista(l1))
	print('min_lista: ', posicion_minimo_lista(l2))

	# test media
	# descomentar las siguientes dos lineas
	print('media: ', media(l1))
	print('media: ', media(l2))

	# test reverso
	# descomentar las siguientes dos lineas
	print('reverso(l1): ', reverso(l1))
	print('reverso(l3): ', reverso(l3))

	# test es_capicua
	# descomentar las siguientes tres lineas
	print('es_capicua(l1): ', es_capicua(l1))
	print('es_capicua(l2): ', es_capicua(l2))
	print('es_capicua(l3): ', es_capicua(l3))

	# test concatenar
	print('concatenar: ', concatenar(l1,l2))

	# test sumar_listas
	# descomentar la siguiente linea
	print('sumar_listas: ', sumar_listas(l1,l2))

	# test quitar_apariciones
	# descomentar las siguientes dos lineas
	quitar_apariciones(l3,'b')
	print('sin aparciones: ', l3)

	# test ordenar_lista
	# descomentar la linea que sigue
	print('sin_ordenar_lista: ', l4)
	print('ordenar_lista: ', ordenar_lista(l4))

	# test fibonacci
	# descomentar las siguientes dos lineas
	print('fibo rec: ', fibo_recursiva(10))
	print('fibo iter: ', fibo_iterativa(10))

if __name__ == '__main__':
	main()

